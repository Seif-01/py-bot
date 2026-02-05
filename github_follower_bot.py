#!/usr/bin/env python3
"""
GitHub Follower Bot - Beginner Friendly Version
Follows all followers of a target GitHub user
"""

import sys

# Check if requests library is installed
try:
    import requests
except ImportError:
    print("\n❌ ERROR: 'requests' library is not installed!")
    print("\n📝 SOLUTION: Open your terminal/command prompt and run:")
    print("   pip install requests")
    print("\nOr if that doesn't work, try:")
    print("   pip3 install requests")
    print("\nThen run this script again.\n")
    sys.exit(1)

import time

class GitHubFollowerBot:
    def __init__(self, token):
        self.token = token
        self.headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        self.base_url = 'https://api.github.com'
    
    def test_token(self):
        """Test if the token is valid"""
        url = f'{self.base_url}/user'
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code == 401:
                print("\n❌ ERROR: Your token is invalid or expired!")
                print("\n📝 SOLUTION:")
                print("1. Go to https://github.com/settings/tokens")
                print("2. Click 'Generate new token (classic)'")
                print("3. Check the 'user:follow' permission")
                print("4. Copy the new token and try again\n")
                return False
            elif response.status_code == 200:
                user_data = response.json()
                print(f"✅ Token valid! Logged in as: {user_data['login']}\n")
                return True
            else:
                print(f"\n⚠️  Warning: Unexpected response: {response.status_code}")
                return False
        except requests.exceptions.ConnectionError:
            print("\n❌ ERROR: Cannot connect to GitHub!")
            print("\n📝 SOLUTION: Check your internet connection and try again.\n")
            return False
        except Exception as e:
            print(f"\n❌ ERROR: {str(e)}\n")
            return False
    
    def get_followers(self, username):
        """Get all followers of a user"""
        followers = []
        page = 1
        
        print(f"📥 Fetching followers of '{username}'...")
        
        while True:
            url = f'{self.base_url}/users/{username}/followers'
            params = {'per_page': 100, 'page': page}
            
            try:
                response = requests.get(url, headers=self.headers, params=params, timeout=10)
                
                if response.status_code == 404:
                    print(f"\n❌ ERROR: User '{username}' not found!")
                    print("\n📝 SOLUTION: Check the spelling and try again.\n")
                    return []
                elif response.status_code != 200:
                    print(f"\n❌ ERROR: GitHub returned error code {response.status_code}")
                    if response.status_code == 403:
                        print("You may have hit the rate limit. Wait an hour and try again.")
                    return []
                
                data = response.json()
                
                if not data:
                    break
                
                followers.extend([user['login'] for user in data])
                print(f"   Page {page} - Total followers found: {len(followers)}")
                page += 1
                
                time.sleep(1)
                
            except requests.exceptions.ConnectionError:
                print("\n❌ ERROR: Lost internet connection!")
                print("📝 SOLUTION: Check your connection and restart the bot.\n")
                return []
            except Exception as e:
                print(f"\n❌ ERROR: {str(e)}\n")
                return []
        
        return followers
    
    def follow_user(self, username):
        """Follow a specific user"""
        url = f'{self.base_url}/user/following/{username}'
        try:
            response = requests.put(url, headers=self.headers, timeout=10)
            return response.status_code == 204
        except:
            return False
    
    def check_if_following(self, username):
        """Check if already following a user"""
        url = f'{self.base_url}/user/following/{username}'
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            return response.status_code == 204
        except:
            return False
    
    def run(self, target_username):
        """Main bot execution"""
        print(f"\n{'='*50}")
        print(f"🤖 Starting GitHub Follower Bot")
        print(f"{'='*50}\n")
        
        # Get all followers
        followers = self.get_followers(target_username)
        
        if not followers:
            print("⚠️  No followers found or an error occurred. Exiting.")
            return
        
        print(f"\n✅ Found {len(followers)} followers to process")
        print(f"\n🚀 Starting to follow users (this may take a while)...\n")
        
        followed_count = 0
        skipped_count = 0
        error_count = 0
        
        for i, follower in enumerate(followers, 1):
            try:
                # Check if already following
                if self.check_if_following(follower):
                    print(f"[{i}/{len(followers)}] ⏭️  Already following {follower}")
                    skipped_count += 1
                    time.sleep(0.5)
                    continue
                
                # Follow the user
                if self.follow_user(follower):
                    print(f"[{i}/{len(followers)}] ✅ Followed {follower}")
                    followed_count += 1
                else:
                    print(f"[{i}/{len(followers)}] ❌ Failed to follow {follower}")
                    error_count += 1
                
                # Wait 2 seconds to avoid rate limits
                time.sleep(2)
                
            except KeyboardInterrupt:
                print("\n\n⚠️  Bot stopped by user (Ctrl+C pressed)")
                print(f"\nProgress so far:")
                print(f"  ✅ Followed: {followed_count}")
                print(f"  ⏭️  Skipped: {skipped_count}")
                print(f"  ❌ Errors: {error_count}\n")
                sys.exit(0)
            except Exception as e:
                print(f"[{i}/{len(followers)}] ❌ Error: {str(e)}")
                error_count += 1
        
        # Final summary
        print(f"\n{'='*50}")
        print(f"🎉 Bot Finished!")
        print(f"{'='*50}")
        print(f"✅ Successfully followed: {followed_count}")
        print(f"⏭️  Skipped (already following): {skipped_count}")
        print(f"❌ Errors: {error_count}")
        print(f"{'='*50}\n")


def main():
    print("\n" + "="*50)
    print("🤖 GitHub Follower Bot - Beginner Friendly")
    print("="*50)
    
    # Get token
    print("\n📌 Step 1: Enter your GitHub Personal Access Token")
    print("   (Don't have one? Visit: https://github.com/settings/tokens)")
    token = input("\n   Token: ").strip()
    
    if not token:
        print("\n❌ ERROR: Token cannot be empty!\n")
        sys.exit(1)
    
    # Create bot and test token
    bot = GitHubFollowerBot(token)
    
    print("\n🔍 Testing your token...")
    if not bot.test_token():
        sys.exit(1)
    
    # Get target username
    print("📌 Step 2: Enter the username whose followers you want to follow")
    target_user = input("\n   Username: ").strip()
    
    if not target_user:
        print("\n❌ ERROR: Username cannot be empty!\n")
        sys.exit(1)
    
    # Confirmation
    print(f"\n⚠️  WARNING:")
    print(f"   This will follow ALL followers of '{target_user}'")
    print(f"   This might take a while depending on how many followers they have.")
    print(f"\n   You can press Ctrl+C at any time to stop the bot.")
    
    confirm = input("\n   Type 'yes' to continue: ").strip().lower()
    
    if confirm != 'yes':
        print("\n✋ Operation cancelled. Goodbye!\n")
        sys.exit(0)
    
    # Run the bot
    bot.run(target_user)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n✋ Bot stopped. Goodbye!\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {str(e)}")
        print("\n📝 If you keep seeing this error:")
        print("   1. Make sure you have internet connection")
        print("   2. Check that your token is valid")
        print("   3. Try running: pip install --upgrade requests\n")
        sys.exit(1)
