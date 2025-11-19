# Quick Installation Guide

## 1. Install the Add-on

### Option A: Manual Installation (Current)

1. **Locate your Anki add-ons folder:**
   - **Windows**: `C:\Users\[username]\AppData\Roaming\Anki2\addons21\`
   - **Mac**: `~/Library/Application Support/Anki2/addons21/`
   - **Linux**: `~/.local/share/Anki2/addons21/`

   Or in Anki: Tools → Add-ons → View Files

2. **Copy this folder:**
   - Copy the entire `anki-ai-assistant` folder into the `addons21` directory
   - The folder should be named something like `anki-ai-assistant` or a number

3. **Restart Anki**
   - Close Anki completely
   - Open it again
   - You should see a tooltip: "AI Card Assistant installed!"

### Option B: From AnkiWeb (Coming Soon)

1. Open Anki
2. Tools → Add-ons → Get Add-ons
3. Enter code: XXXXXX
4. Click OK
5. Restart Anki

## 2. Get Your API Key

1. Go to https://console.anthropic.com
2. Sign up or log in
3. Click "API Keys" in the left sidebar
4. Click "Create Key"
5. Give it a name (e.g., "Anki Add-on")
6. Copy the key (starts with `sk-ant-...`)
7. **Save it somewhere safe!** (You won't see it again)

## 3. Configure the Add-on

1. In Anki: **Tools → AI Assistant Settings**
2. Paste your API key in the "API Key" field
3. Click **"Test API Key"** to verify it works
4. If successful, click **"Save"**

## 4. Try It Out!

1. Open a deck and start reviewing
2. When you see a card, look for the **"🤖 Ask AI"** button at the bottom
3. Click it (or press `Ctrl+Shift+A`)
4. Select "Simplify the explanation" or "Add a practical example"
5. Click **"Ask AI"**
6. Wait a few seconds
7. Review the response
8. Click **"Apply to Card"** if you like it!

## Troubleshooting

### "Add-on not loading"
- Check that the folder is in the right place
- Restart Anki
- Check Tools → Add-ons to see if it's listed
- Look for errors in Tools → Add-ons → [select add-on] → View Files → check errors

### "No button appears"
- Make sure you're in review mode (reviewing cards, not browsing)
- Restart Anki
- Check if other add-ons are conflicting

### "Invalid API Key"
- Make sure you copied the entire key
- Check for extra spaces
- Verify it's activated at console.anthropic.com
- Try creating a new key

### "It's too expensive!"
It's not! Typical costs:
- Per query: $0.003 - $0.008 (less than a penny)
- Per month: $0.50 - $2.00 for regular use
- That's less than a coffee!

## What's Next?

- Read the [full README](README.md) for all features
- Check out example use cases
- Join the community discussion
- Report bugs or suggest features

## Need Help?

- Check the README: Common questions answered
- GitHub Issues: Report bugs
- AnkiWeb Reviews: Share your experience

---

**You're all set! Happy learning! 🚀**
