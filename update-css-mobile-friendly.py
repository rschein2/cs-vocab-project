#!/usr/bin/env python3
"""
Update all old flashcard HTML files to use mobile-friendly CSS formatting.
This fixes the horizontal scrolling issue on mobile devices.
"""

import re
import glob

# Old CSS pattern (with overflow-x: auto)
OLD_PRE_CSS = r'''        pre \{
            background-color: rgba\(127, 127, 127, 0\.15\);
            padding: 12px;
            border-radius: 5px;
            overflow-x: auto;
            margin: 10px 0;
        \}

        pre code \{
            background-color: transparent;
            padding: 0;
        \}'''

# New mobile-friendly CSS (with word-wrap and smaller font)
NEW_PRE_CSS = '''        pre {
            background-color: rgba(127, 127, 127, 0.15);
            padding: 12px;
            border-radius: 5px;
            margin: 10px 0;
            font-size: 0.75em;
        }

        pre code {
            background-color: transparent;
            padding: 0;
            white-space: pre-wrap;
            word-wrap: break-word;
        }'''

# Get all HTML files except the new ones (which already have the correct CSS)
exclude_files = [
    'nlp-transformers-flashcards.html',
    'model-evaluation-metrics-flashcards.html',
    'advanced-pytorch-flashcards.html',
    'mlops-langfuse-flashcards.html'
]

html_files = [f for f in glob.glob('*-flashcards.html') if f not in exclude_files]

print(f'Updating CSS in {len(html_files)} HTML files...')
print()

updated_count = 0
for html_file in sorted(html_files):
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if file has old CSS
        if re.search(OLD_PRE_CSS, content):
            # Replace old CSS with new CSS
            new_content = re.sub(OLD_PRE_CSS, NEW_PRE_CSS, content)

            # Write back to file
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(new_content)

            print(f'✓ Updated: {html_file}')
            updated_count += 1
        else:
            print(f'- Skipped: {html_file} (already has new CSS or different format)')

    except Exception as e:
        print(f'✗ Error updating {html_file}: {e}')

print()
print('=' * 60)
print(f'Done! Updated {updated_count} files.')
print()
print('Next steps:')
print('1. Run: python3 generate-anki-packages.py')
print('2. Import the updated .apkg files into Anki')
print('   (This will update your existing decks with mobile-friendly formatting)')
