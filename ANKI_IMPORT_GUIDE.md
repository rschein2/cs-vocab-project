# Anki Import Guide

This guide explains how to import the CS Vocab flashcards into Anki with the proper subdeck structure.

## Subdeck Structure

When imported correctly, your cards will appear as:

```
CS Vocab/
├── Git (32 cards)
├── tmux (18 cards)
└── SSH (20 cards)
```

This lets you:
- Study all CS topics together (study "CS Vocab")
- Or study specific topics individually (study "CS Vocab::Git" only)
- Mix and match what you want to learn

## Method 1: Import Text Files (Recommended)

The `.txt` files are pre-formatted for Anki import with deck names embedded.

### Steps:

1. **Open Anki**

2. **Import the file:**
   - File → Import
   - Select `git-anki-import.txt` (or tmux/ssh)

3. **Import settings will auto-detect:**
   - Type: Basic (and reversed card if you want)
   - Deck: `CS Vocab::Git` (already specified in file)
   - Fields separated by: Tab
   - Allow HTML in fields: Yes (auto-detected from `#html:true`)

4. **Click Import**

5. **Repeat for other topics:**
   - Import `tmux-anki-import.txt` → creates `CS Vocab::tmux`
   - Import `ssh-anki-import.txt` → creates `CS Vocab::SSH`

### Result:

You'll see a parent deck called "CS Vocab" with three subdecks inside it.

## Method 2: Import HTML Files (Manual)

If you prefer to work with the HTML files:

1. **Create the deck structure first:**
   - In Anki, click "Create Deck"
   - Name it: `CS Vocab::Git`
   - Repeat for `CS Vocab::tmux` and `CS Vocab::SSH`

2. **Select target deck** before importing

3. **Open the HTML file in a browser**
   - Navigate to each card
   - Copy the "front" content → paste into Anki front field
   - Copy the "back" content → paste into Anki back field
   - Add tags: `cs`, `git`, `EN` (or `tmux`/`ssh`)

This method is tedious but gives you full control.

## Method 3: Use the .apkg Package (Coming Soon)

For the easiest import, we can create `.apkg` files (Anki packages) that include:
- Pre-built deck structure
- All cards formatted correctly
- Tags applied
- No manual steps needed

To generate these, install `genanki`:

```bash
pip install genanki
python3 generate-anki-packages.py
```

Then just double-click the `.apkg` files to import!

## Understanding the Deck Naming

The `::` syntax creates hierarchy:

- `CS Vocab::Git` → Creates "CS Vocab" parent, "Git" child
- `CS Vocab::tmux::Advanced` → Creates "CS Vocab" → "tmux" → "Advanced"
- `Work::Projects::Client-A` → Three levels deep

## Customizing the Structure

Want different organization? Edit the `#deck:` line in the `.txt` files:

```
#deck:CS Vocab::Git           # Original
#deck:Programming::Git         # Changed parent
#deck:DevOps::Version Control  # Different structure
#deck:Git                      # No parent (top-level deck)
```

## Importing Only What You Need

**Want just SSH and tmux?**
- Only import `ssh-anki-import.txt` and `tmux-anki-import.txt`
- You'll get `CS Vocab` deck with only those two subdecks

**Want to rename the parent deck?**
- Edit the `.txt` files before importing
- Change `#deck:CS Vocab::SSH` to `#deck:DevOps::SSH`

## Tips for Studying

1. **Start with one subdeck:** Master Git before moving to SSH
2. **Use Anki's "Custom Study":** Create sessions mixing different subdecks
3. **Adjust new cards/day:** Start with 5-10 cards per deck
4. **Be honest with yourself:** If you hesitated, mark it "Again"
5. **Actually type the commands:** Muscle memory matters!

## Troubleshooting

**Cards imported but not in subdecks?**
- Check the `#deck:` line in the `.txt` file
- Make sure you didn't manually select a different deck during import

**HTML not rendering?**
- Ensure "Allow HTML in fields" is checked during import
- The `#html:true` directive should handle this automatically

**Tags not applied?**
- The `#tags column:3` directive tells Anki the third column is tags
- If missing, you can bulk-add tags later in Anki browser

**Want to merge with existing decks?**
- If you already have a "Git" deck, import into `Git` instead of `CS Vocab::Git`
- Or rename your existing deck to `CS Vocab::Git` first

## Next Steps

After importing, check out the README.md for:
- The philosophy behind these cards
- How to study effectively with spaced repetition
- Why this approach works for CS systems knowledge

Happy learning!
