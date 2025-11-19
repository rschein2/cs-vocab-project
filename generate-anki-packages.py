#!/usr/bin/env python3
"""
Generate Anki package files (.apkg) for CS Vocab flashcards.

Usage:
    pip install genanki
    python3 generate-anki-packages.py

Outputs:
    - cs-vocab-git.apkg
    - cs-vocab-tmux.apkg
    - cs-vocab-ssh.apkg
    - cs-vocab-all.apkg (combined package)
"""

import re
import random

try:
    import genanki
except ImportError:
    print("Error: genanki not installed")
    print("Install with: pip install genanki")
    print("Then run this script again")
    exit(1)


def extract_cards_from_html(filename):
    """Extract cards from HTML file and return as list of dicts"""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all card divs
    card_pattern = r'<!-- Card \d+ -->\s*<div class="card">(.*?)</div>\s*(?=<!-- Card|\s*</body>)'
    cards = re.findall(card_pattern, content, re.DOTALL)

    extracted = []
    for card_html in cards:
        # Extract front
        front_match = re.search(r'<div class="front">(.*?)</div>', card_html, re.DOTALL)
        # Extract back
        back_match = re.search(r'<div class="back">(.*?)</div>\s*<div class="tags">', card_html, re.DOTALL)
        # Extract tags
        tags_match = re.search(r'<div class="tags">(.*?)</div>', card_html, re.DOTALL)

        if front_match and back_match and tags_match:
            front = front_match.group(1).strip()
            back = back_match.group(1).strip()
            tags = tags_match.group(1).strip().split()

            extracted.append({
                'front': front,
                'back': back,
                'tags': tags
            })

    return extracted


# Define the card model (same for all decks)
CS_VOCAB_MODEL = genanki.Model(
    1607392319,  # Random model ID
    'CS Vocab Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '''
                <div class="question">
                    {{Question}}
                </div>
            ''',
            'afmt': '''
                <div class="question">
                    {{Question}}
                </div>
                <hr>
                <div class="answer">
                    {{Answer}}
                </div>
            ''',
        },
    ],
    css='''
        .card {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            font-size: 16px;
            text-align: left;
            color: #333;
            background-color: white;
            padding: 20px;
        }

        .question {
            font-size: 1.2em;
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 20px;
        }

        .answer {
            line-height: 1.6;
            color: #555;
        }

        code {
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
            font-size: 0.9em;
            color: #c7254e;
        }

        pre {
            background-color: #f4f4f4;
            padding: 12px;
            border-radius: 5px;
            overflow-x: auto;
            margin: 10px 0;
        }

        pre code {
            background-color: transparent;
            padding: 0;
            color: #333;
        }

        strong {
            color: #2c3e50;
            font-weight: 600;
        }

        ul, ol {
            margin: 10px 0;
            padding-left: 30px;
        }

        li {
            margin: 5px 0;
        }

        hr {
            border: none;
            border-top: 2px solid #e0e0e0;
            margin: 20px 0;
        }
    '''
)


def create_deck_package(html_file, deck_name, output_file, deck_id):
    """Create an Anki package from HTML file"""

    # Create deck with proper naming for subdecks
    deck = genanki.Deck(
        deck_id,
        deck_name
    )

    # Extract cards
    cards = extract_cards_from_html(html_file)

    # Add cards to deck
    for card_data in cards:
        note = genanki.Note(
            model=CS_VOCAB_MODEL,
            fields=[card_data['front'], card_data['back']],
            tags=card_data['tags']
        )
        deck.add_note(note)

    # Create package
    package = genanki.Package(deck)
    package.write_to_file(output_file)

    print(f'✓ Created {output_file} - {len(cards)} cards in deck "{deck_name}"')
    return deck


def create_combined_package(decks, output_file):
    """Create a single package with multiple decks"""
    package = genanki.Package(decks)
    package.write_to_file(output_file)
    total_cards = sum(len(deck.notes) for deck in decks)
    print(f'✓ Created {output_file} - {total_cards} total cards across {len(decks)} decks')


if __name__ == '__main__':
    print('CS Vocab Anki Package Generator')
    print('=' * 50)
    print()

    # Generate individual packages
    decks = []

    deck_configs = [
        ('git-flashcards.html', 'CS Vocab::Git', 'cs-vocab-git.apkg', 2059400110),
        ('tmux-flashcards.html', 'CS Vocab::tmux', 'cs-vocab-tmux.apkg', 2059400111),
        ('ssh-flashcards.html', 'CS Vocab::SSH', 'cs-vocab-ssh.apkg', 2059400112),
        ('linux-shell-flashcards.html', 'CS Vocab::Linux Shell', 'cs-vocab-linux.apkg', 2059400113),
        ('linux-utilities-flashcards.html', 'CS Vocab::Linux Utilities', 'cs-vocab-linux-utils.apkg', 2059400114),
        ('linux-processes-flashcards.html', 'CS Vocab::Linux Processes', 'cs-vocab-processes.apkg', 2059400115),
        ('readline-shortcuts-flashcards.html', 'CS Vocab::Readline Shortcuts', 'cs-vocab-readline.apkg', 2059400116),
        ('shell-scripting-flashcards.html', 'CS Vocab::Shell Scripting', 'cs-vocab-scripting.apkg', 2059400117),
        ('regex-flashcards.html', 'CS Vocab::Regex Patterns', 'cs-vocab-regex.apkg', 2059400118),
        ('networking-flashcards.html', 'CS Vocab::Networking', 'cs-vocab-networking.apkg', 2059400119),
        ('filesystem-flashcards.html', 'CS Vocab::File System Hierarchy', 'cs-vocab-filesystem.apkg', 2059400120),
        ('shell-config-flashcards.html', 'CS Vocab::Shell Configuration', 'cs-vocab-shell-config.apkg', 2059400121),
    ]

    for html_file, deck_name, output_file, deck_id in deck_configs:
        try:
            deck = create_deck_package(html_file, deck_name, output_file, deck_id)
            decks.append(deck)
        except FileNotFoundError:
            print(f'✗ Error: {html_file} not found')
        except Exception as e:
            print(f'✗ Error creating {output_file}: {e}')

    # Generate combined package
    if decks:
        print()
        create_combined_package(decks, 'cs-vocab-all.apkg')

    print()
    print('=' * 50)
    print('Done! Import the .apkg files into Anki.')
    print()
    print('Individual packages:')
    print('  - cs-vocab-git.apkg         (Git only)')
    print('  - cs-vocab-tmux.apkg        (tmux only)')
    print('  - cs-vocab-ssh.apkg         (SSH only)')
    print('  - cs-vocab-linux.apkg       (Linux Shell only)')
    print('  - cs-vocab-linux-utils.apkg (Linux Utilities only)')
    print('  - cs-vocab-processes.apkg   (Linux Processes only)')
    print('  - cs-vocab-readline.apkg    (Readline/Bash Shortcuts only)')
    print('  - cs-vocab-scripting.apkg   (Shell Scripting only)')
    print('  - cs-vocab-regex.apkg       (Regex Patterns only)')
    print('  - cs-vocab-networking.apkg  (Networking only)')
    print('  - cs-vocab-filesystem.apkg  (File System Hierarchy only)')
    print('  - cs-vocab-shell-config.apkg (Shell Configuration only)')
    print()
    print('Combined package:')
    print('  - cs-vocab-all.apkg         (All topics)')
    print()
    print('Import creates subdeck structure: CS Vocab → Git/tmux/SSH/Linux Shell/Linux Utilities/Linux Processes/Readline Shortcuts/Shell Scripting/Regex Patterns/Networking/File System Hierarchy/Shell Configuration')
