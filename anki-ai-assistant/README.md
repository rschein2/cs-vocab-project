# AI Card Assistant for Anki

**Transform your flashcard learning with AI-powered assistance!**

Ask questions, get clarifications, create related cards, and refine your knowledge - all while reviewing.

## Features

🤖 **AI-Powered Card Refinement**
- Simplify complex explanations
- Add practical examples
- Create mnemonics and memory aids
- Generate related cards automatically

💬 **Interactive Learning**
- Ask custom questions about any card
- Get instant clarifications
- Request alternative explanations
- "Explain like I'm 5" mode

✨ **Smart Integration**
- One-click access during review
- Context-aware (knows your deck, tags)
- Preview before applying changes
- Auto-tags AI-generated cards

💰 **Cost-Effective**
- Uses your own API key (full control)
- ~$0.003 - $0.008 per query
- Typical usage: $0.50 - $2.00/month
- Pay only for what you use

## Installation

### Step 1: Install the Add-on

**Method A: From File** (recommended for now)
1. Download the `anki-ai-assistant` folder
2. Open Anki → Tools → Add-ons → View Files
3. Copy the `anki-ai-assistant` folder into the addons21 directory
4. Restart Anki

**Method B: AnkiWeb** (coming soon)
1. Tools → Add-ons → Get Add-ons
2. Enter code: XXXXXX (pending submission)
3. Restart Anki

### Step 2: Get Your API Key

1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Sign up or log in
3. Navigate to API Keys
4. Create a new key
5. Copy it (starts with `sk-ant-...`)

**Cost:**
- No monthly subscription
- Pay only for usage
- First $5 in credits (check Anthropic for current promotions)
- Typical student usage: $0.50 - $2.00/month

### Step 3: Configure

1. In Anki: Tools → AI Assistant Settings
2. Paste your API key
3. Click "Test API Key" to verify
4. Click "Save"

Done! 🎉

## Usage

### During Review

**Button Method:**
1. Review a card
2. Click "🤖 Ask AI" button at bottom
3. Choose an action or ask a custom question
4. Click "Ask AI"
5. Review response
6. Apply to card (or not)

**Keyboard Shortcut:**
- Press `Ctrl+Shift+A` on any card
- Same dialog opens

### Available Actions

1. **Ask a custom question**
   - "What's a real-world example of this?"
   - "Why does this work this way?"
   - "How does this relate to X?"

2. **Simplify the explanation**
   - Rewrites in clearer, more accessible language
   - Perfect for overly technical cards

3. **Add a practical example**
   - Generates real-world scenarios
   - Makes abstract concepts concrete

4. **Clarify a confusing part**
   - Identifies potential confusion points
   - Provides additional context

5. **Create a related card**
   - Generates complementary flashcards
   - Builds connected knowledge

6. **Add mnemonics or memory aids**
   - Creates memory tricks
   - Makes cards more memorable

7. **Explain like I'm 5**
   - Ultra-simple explanations
   - Great for complex topics

8. **Add alternative explanations**
   - Different perspectives
   - Multiple mental models

### Applying Changes

After getting a response, you can:

- **Replace**: Overwrites the back of the card
- **Append**: Adds to existing content
- **Create New Card**: For "related card" suggestions
- **Just Read**: Learn without changing the card

## Examples

### Example 1: Simplifying

**Original Card:**
- Front: "What is polymorphism?"
- Back: "Polymorphism is a core concept in OOP that enables objects of different classes to be treated as objects of a common superclass, achieved through inheritance and interfaces."

**After "Simplify":**
- Back: "Polymorphism lets you use different types of objects interchangeably. Example: Both `Dog` and `Cat` can be treated as `Animal`, so you can write code that works with any animal type."

### Example 2: Adding Examples

**Original:**
- Front: "What does git rebase do?"
- Back: "Reapplies commits on top of another base tip"

**After "Add practical example":**
- Back: "Reapplies commits on top of another base tip

  **Example:** You're working on a feature branch while main has new commits. Instead of merging, rebase moves your feature commits to the tip of main, creating a linear history.

  ```
  git checkout feature
  git rebase main
  ```"

### Example 3: Creating Related Cards

**Original Card:**
- "What's the difference between `let` and `const` in JavaScript?"

**AI Generates:**
- Front: "When should you use `const` vs `let` in JavaScript?"
- Back: "Use `const` by default for values that won't be reassigned. Use `let` only when you need to reassign. This makes code more predictable and prevents accidental mutations."

## Settings

### Model Selection

- **Claude Sonnet 4** (default): Best balance of quality and cost
- **Claude 3.5 Sonnet**: Slightly faster, good quality
- **Claude 3 Opus**: Highest quality, more expensive

### Max Tokens

- **512**: Short, concise responses
- **1024** (default): Good balance
- **2048+**: Longer, more detailed responses

Higher = better quality but more expensive

### Options

- **Show cost estimates**: Display estimated cost before queries
- **Auto-tag AI cards**: Tag generated cards with `ai-generated`

## FAQ

**Q: How much does this cost?**
A: ~$0.003 - $0.008 per query. Typical usage: $0.50 - $2.00/month.

**Q: Do I need a subscription?**
A: No! You pay only for API usage (per query), not a monthly fee.

**Q: Is my data safe?**
A: Your cards are sent to Anthropic's API for processing. See [Anthropic's privacy policy](https://www.anthropic.com/privacy). API key is stored locally in Anki.

**Q: Can I use OpenAI instead?**
A: Not yet, but we're adding OpenAI support soon! For now, Anthropic Claude only.

**Q: Does this work on mobile?**
A: The add-on runs on Anki Desktop only. Mobile apps don't support add-ons.

**Q: Will this make me learn worse?**
A: No! It's a tool to help you *understand* better. You still do the active recall. Think of it as having a tutor available 24/7.

**Q: Can I use this offline?**
A: No, it requires internet to call the AI API.

**Q: What if I run out of API credits?**
A: Add more credits to your Anthropic account. The add-on will show an error if API calls fail.

## Tips

1. **Start with standard actions** before custom questions
2. **Review before applying** - AI isn't perfect!
3. **Use "Append"** to keep original content
4. **Tag AI cards** to track what you've modified
5. **Ask follow-ups** - click "Ask AI" multiple times on same card
6. **Create card families** - use "related card" to build connected knowledge

## Troubleshooting

**"Invalid API Key" error:**
- Check you copied the full key (starts with `sk-ant-`)
- Verify it's activated at console.anthropic.com
- Try creating a new key

**"Rate limit exceeded":**
- You're sending too many requests
- Wait a minute and try again
- Check your usage at console.anthropic.com

**"Network error":**
- Check your internet connection
- Verify firewall isn't blocking Anthropic API
- Try again in a moment

**Button doesn't appear:**
- Restart Anki
- Check add-on is enabled (Tools → Add-ons)
- Check for conflicts with other add-ons

**Response is cut off:**
- Increase "Max Tokens" in settings
- Reword your question to be more specific

## Contributing

Found a bug? Have a feature idea?

- GitHub: [your-repo-url]
- Email: [your-email]
- AnkiWeb Reviews

## Roadmap

- [ ] OpenAI GPT support
- [ ] Bulk processing (enhance multiple cards at once)
- [ ] Learning analytics (track AI usage, improvements)
- [ ] Card templates for specific subjects
- [ ] Collaborative card improvement
- [ ] Voice input for questions
- [ ] Image analysis (for image occlusion cards)

## License

MIT License - feel free to modify and share!

## Credits

Built with ❤️ for the Anki community

Powered by [Anthropic Claude](https://www.anthropic.com)

---

**Happy learning! 🚀**

If this add-on helps you, consider:
- ⭐ Starring on GitHub
- 📝 Leaving a review on AnkiWeb
- 💬 Sharing with fellow students
