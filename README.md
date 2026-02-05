# 🚀 GUIDE - GitHub Follower Bot

# FEEL FREE TO ADD OR EDIT THIS CODE TO YOUR LIKING

Follow these steps exactly and you'll be fine.

---

### Step 1: Install Python (if you don't have it)

**Check if you have Python:**
1. Open Terminal (Mac) or Command Prompt (Windows)
2. Type: `python --version` and press Enter
3. If you see something like "Python 3.x.x" → You're good! Skip to Step 2
4. If you get an error → Download Python from https://www.python.org/downloads/

**Windows users:** During installation, CHECK the box that says "Add Python to PATH"!

---

### Step 2: Download the Bot Files

1. Download these 3 files:
   - `github_follower_bot.py`
   - `requirements.txt`

2. Put them all in the **same folder** (example create a folder called `github-followers-bot`)

---

### Step 3: Install the Required Library

**Open Terminal/Command Prompt** and navigate to your folder:

```bash
cd path/to/your/github-followers-bot
```

**Example:**
- Windows: `cd C:\Users\YourName\Downloads\github-followers-bot`
- Mac: `cd ~/Downloads/github-followers-bot`

Then run:
```bash
pip install -r requirements.txt
```

**If that doesn't work, try:**
```bash
pip3 install -r requirements.txt
```

**OR just install directly:**
```bash
pip install requests
```

You should see "Successfully installed requests"

---

### Step 4: Get Your GitHub Token

**This is the key that lets the bot access your account:**

1. Log into GitHub in your browser
2. Go to: https://github.com/settings/tokens
3. Click **"Generate new token"** → Select **"Generate new token (classic)"**
4. Give it a name like "Follower Bot"
5. Under "Select scopes", find and CHECK: **`user:follow`**
6. Scroll down and click **"Generate token"**
7. **IMPORTANT:** Copy the token immediately (starts with `ghp_`)
   - You won't be able to see it again!
   - Paste it somewhere safe for now

---

### Step 5: Run the Bot! 🎉

In your Terminal/Command Prompt (still in the github-bot folder):

```bash
python github_follower_bot.py
```

**If that doesn't work, try:**
```bash
python3 github_follower_bot.py
```

The bot will ask you:

1. **"Token:"** → Paste your token (from Step 4) and press Enter
2. **"Username:"** → Type the GitHub username whose followers you want to follow
3. **Confirmation:** Type `yes` and press Enter

Then sit back and watch! ☕

---

## 🆘 COMMON ERRORS & HOW TO FIX THEM

### ❌ "requests library is not installed"
**FIX:** Run `pip install requests` or `pip3 install requests`

---

### ❌ "python is not recognized as a command"
**FIX:** 
- **Windows:** Reinstall Python and CHECK "Add Python to PATH"
- **Mac:** Use `python3` instead of `python`

---

### ❌ "Your token is invalid or expired"
**FIX:**
1. Go to https://github.com/settings/tokens
2. Delete the old token
3. Generate a NEW token (see Step 4 above)
4. Make sure you check the **`user:follow`** permission!

---

### ❌ "User 'xyz' not found"
**FIX:** 
- Check the spelling of the username
- Make sure the username exists on GitHub

---

### ❌ "Cannot connect to GitHub"
**FIX:** Check your internet connection

---

### ❌ "Rate limit exceeded"
**FIX:** 
- Wait 1 hour (GitHub limits how many requests you can make)
- The bot automatically handles this, but if you run it too many times, you'll hit the limit

---

## 🛑 HOW TO STOP THE BOT

Press **Ctrl+C** (hold Ctrl and press C) at any time to stop the bot.

It will show you how many people it followed before stopping.

---

## ⚠️ IMPORTANT TIPS

1. **Don't share your token** - It's like a password!
2. **Delete tokens you're not using** - Go to https://github.com/settings/tokens
note : Make sure to give "follower" permission
3. **Be patient** - The bot waits 2 seconds between each follow to avoid getting banned
4. **Use responsibly** - Don't spam or annoy people

---

## 📞 STILL STUCK?

If you see an error that's not listed here:

1. Read the error message carefully - it often tells you what's wrong
2. Google the error message
3. Make sure you:
   - Have internet connection
   - Installed `requests` library
   - Generated a valid token with `user:follow` permission
   - Spelled the username correctly

---

## 🎯 WHAT DOES THE BOT DO?

1. Logs into GitHub using your token
2. Finds all followers of the person you specify
3. Follows each of them one by one
4. Skips people you already follow
5. Gives you a summary at the end

FEEL FREE TO ADD OR EDIT THIS CODE TO YOUR LIKING
