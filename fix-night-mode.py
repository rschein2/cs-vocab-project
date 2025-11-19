#!/usr/bin/env python3
"""
Fix CSS in all flashcard HTML files to work in both light and night modes
"""

import re
import glob

# New CSS that works in both modes
NIGHT_MODE_CSS = '''    <style>
        .card {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            font-size: 18px;
            line-height: 1.6;
            padding: 20px;
        }

        /* Code blocks */
        code {
            background-color: rgba(127, 127, 127, 0.2);
            padding: 2px 6px;
            border-radius: 3px;
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
            font-size: 0.9em;
        }

        pre {
            background-color: rgba(127, 127, 127, 0.15);
            padding: 12px;
            border-radius: 5px;
            overflow-x: auto;
            margin: 10px 0;
        }

        pre code {
            background-color: transparent;
            padding: 0;
        }

        strong {
            font-weight: 600;
        }

        ul, ol {
            margin: 10px 0;
            padding-left: 30px;
        }

        li {
            margin: 5px 0;
        }

        /* Note boxes */
        .note {
            background-color: rgba(23, 162, 184, 0.15);
            border-left: 4px solid rgba(23, 162, 184, 0.8);
            padding: 10px;
            margin: 10px 0;
            border-radius: 3px;
        }

        .warning {
            background-color: rgba(220, 53, 69, 0.15);
            border-left: 4px solid rgba(220, 53, 69, 0.8);
            padding: 10px;
            margin: 10px 0;
            border-radius: 3px;
        }

        .tip {
            background-color: rgba(255, 193, 7, 0.15);
            border-left: 4px solid rgba(255, 193, 7, 0.8);
            padding: 10px;
            margin: 10px 0;
            border-radius: 3px;
        }

        hr {
            border: none;
            border-top: 1px solid rgba(127, 127, 127, 0.3);
            margin: 15px 0;
        }

        /* Night mode specific adjustments */
        .nightMode code {
            color: #ff79c6;
        }

        .nightMode strong {
            color: #8be9fd;
        }
    </style>'''

def fix_html_file(filepath):
    """Fix CSS in a single HTML file"""
    print(f"Fixing {filepath}...")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the entire <style> section
    # Find style tag and replace everything between <style> and </style>
    pattern = r'<style>.*?</style>'

    # Replace with new CSS
    new_content = re.sub(pattern, NIGHT_MODE_CSS, content, flags=re.DOTALL)

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"  ✓ Fixed {filepath}")

def main():
    # Find all flashcard HTML files
    html_files = glob.glob('*-flashcards.html')

    if not html_files:
        print("No flashcard HTML files found!")
        return

    print(f"Found {len(html_files)} flashcard files")
    print()

    for filepath in html_files:
        fix_html_file(filepath)

    print()
    print("=" * 50)
    print("All files fixed!")
    print("Now regenerate the Anki packages:")
    print("  python3 generate-anki-packages.py")

if __name__ == '__main__':
    main()
