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

    # Try new format first (ML flashcards)
    # Pattern matches: <div class="card">...</div> with proper nesting
    card_pattern = r'<div class="card">\s*<h3>(.*?)</h3>(.*?)(?=<div class="card">|</body>)'
    matches = re.findall(card_pattern, content, re.DOTALL)

    extracted = []

    if matches:
        # New format: Question/Answer with h4 tags
        for deck_name, card_content in matches:
            # Check if it's a cloze card (has {{c1::...}})
            if '{{c' in card_content:
                # Cloze card: Question becomes both front and back
                question_match = re.search(r'<h4>Question:</h4>\s*<p>(.*?)</p>', card_content, re.DOTALL)
                if question_match:
                    question = question_match.group(1).strip()
                    extracted.append({
                        'front': question,
                        'back': question,
                        'tags': ['cloze']
                    })
            else:
                # Regular Q&A card
                question_match = re.search(r'<h4>Question:</h4>\s*<p>(.*?)</p>', card_content, re.DOTALL)
                answer_match = re.search(r'<h4>Answer:</h4>(.*?)$', card_content, re.DOTALL)

                if question_match and answer_match:
                    question = question_match.group(1).strip()
                    answer = answer_match.group(1).strip()
                    extracted.append({
                        'front': question,
                        'back': answer,
                        'tags': []
                    })
    else:
        # Old format: front/back/tags divs
        card_pattern = r'(?:<!-- Card \d+ -->\s*)?<div class="card">(.*?)</div>\s*(?=(?:<!-- Card|<div class="card">)|\s*</body>)'
        cards = re.findall(card_pattern, content, re.DOTALL)

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


# Define the card models
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
            padding: 20px;
            line-height: 1.6;
        }

        .question {
            font-size: 1.2em;
            font-weight: 600;
            margin-bottom: 20px;
        }

        .answer {
            line-height: 1.6;
        }

        code {
            background-color: rgba(127, 127, 127, 0.2);
            padding: 2px 6px;
            border-radius: 3px;
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
            font-size: 0.9em;
        }

        .nightMode code {
            color: #ff79c6;
        }

        pre {
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
        }

        strong {
            font-weight: 600;
        }

        .nightMode strong {
            color: #8be9fd;
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
            border-top: 2px solid rgba(127, 127, 127, 0.3);
            margin: 20px 0;
        }
    '''
)

# Cloze model for cards with {{c1::...}} deletions
CS_VOCAB_CLOZE_MODEL = genanki.Model(
    1607392320,  # Different model ID
    'CS Vocab Cloze Model',
    fields=[
        {'name': 'Text'},
    ],
    templates=[
        {
            'name': 'Cloze',
            'qfmt': '{{cloze:Text}}',
            'afmt': '{{cloze:Text}}',
        },
    ],
    model_type=genanki.Model.CLOZE,
    css='''
        .card {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            font-size: 16px;
            text-align: left;
            padding: 20px;
            line-height: 1.6;
        }

        .cloze {
            font-weight: bold;
            color: #0066cc;
        }

        code {
            background-color: rgba(127, 127, 127, 0.2);
            padding: 2px 6px;
            border-radius: 3px;
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
            font-size: 0.9em;
        }

        .nightMode code {
            color: #ff79c6;
        }

        pre {
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
        }

        strong {
            font-weight: 600;
        }

        .nightMode strong {
            color: #8be9fd;
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
        # Use cloze model if card has cloze tag
        if 'cloze' in card_data['tags']:
            note = genanki.Note(
                model=CS_VOCAB_CLOZE_MODEL,
                fields=[card_data['front']],
                tags=card_data['tags']
            )
        else:
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
        ('find-tree-flashcards.html', 'CS Vocab::Find and Tree Commands', 'cs-vocab-find.apkg', 2059400122),
        ('package-diff-flashcards.html', 'CS Vocab::Package Management & Diff', 'cs-vocab-package-diff.apkg', 2059400123),
        ('text-processing-flashcards.html', 'CS Vocab::Text Processing', 'cs-vocab-text.apkg', 2059400124),
        ('permissions-flashcards.html', 'CS Vocab::Permissions & Ownership', 'cs-vocab-permissions.apkg', 2059400125),
        ('archives-compression-flashcards.html', 'CS Vocab::Archives & Compression', 'cs-vocab-archives.apkg', 2059400126),
        ('logs-monitoring-flashcards.html', 'CS Vocab::System Logs & Monitoring', 'cs-vocab-logs.apkg', 2059400127),
        ('users-groups-flashcards.html', 'CS Vocab::User & Group Management', 'cs-vocab-users.apkg', 2059400128),
        ('disk-management-flashcards.html', 'CS Vocab::Disk Management', 'cs-vocab-disk.apkg', 2059400129),
        ('symlinks-attributes-flashcards.html', 'CS Vocab::Symbolic Links & File Attributes', 'cs-vocab-symlinks.apkg', 2059400130),
        ('xargs-chaining-flashcards.html', 'CS Vocab::xargs & Command Chaining', 'cs-vocab-xargs.apkg', 2059400131),
        ('grep-deep-dive-flashcards.html', 'CS Vocab::Grep Deep Dive', 'cs-vocab-grep.apkg', 2059400132),
        ('gcloud-ml-training-flashcards.html', 'CS Vocab::GCloud ML Training', 'cs-vocab-gcloud.apkg', 2059400133),
        ('vscode-productivity-flashcards.html', 'CS Vocab::VSCode Productivity', 'cs-vocab-vscode.apkg', 2059400134),
        ('bash-history-flashcards.html', 'CS Vocab::Bash History & Command Recall', 'cs-vocab-history.apkg', 2059400135),
        ('job-control-flashcards.html', 'CS Vocab::Job Control', 'cs-vocab-job-control.apkg', 2059400136),
        ('redirection-pipes-flashcards.html', 'CS Vocab::Redirection & Pipes', 'cs-vocab-redirection.apkg', 2059400137),
        ('environment-variables-flashcards.html', 'CS Vocab::Environment Variables & PATH', 'cs-vocab-env-vars.apkg', 2059400138),
        ('quoting-escaping-flashcards.html', 'CS Vocab::Quoting & Escaping', 'cs-vocab-quoting.apkg', 2059400139),
        ('exit-status-flashcards.html', 'CS Vocab::Exit Status & Return Codes', 'cs-vocab-exit-status.apkg', 2059400140),
        ('brace-expansion-globbing-flashcards.html', 'CS Vocab::Brace Expansion & Globbing', 'cs-vocab-globbing.apkg', 2059400141),
        ('aliases-functions-scripts-flashcards.html', 'CS Vocab::Aliases, Functions & Scripts', 'cs-vocab-functions.apkg', 2059400142),
        ('ci-continuous-integration-flashcards.html', 'CS Vocab::CI/Continuous Integration', 'cs-vocab-ci.apkg', 2059400143),
        ('linux-history-trivia-flashcards.html', 'CS Vocab::Linux History & Trivia', 'cs-vocab-linux-history.apkg', 2059400144),
        ('sed-deep-dive-flashcards.html', 'CS Vocab::Sed Deep Dive', 'cs-vocab-sed.apkg', 2059400145),
        ('linux-sociopolitical-flashcards.html', 'CS Vocab::Linux Sociopolitical History', 'cs-vocab-sociopolitical.apkg', 2059400146),
        ('common-cli-errors-flashcards.html', 'CS Vocab::Common CLI Errors & Antipatterns', 'cs-vocab-common-errors.apkg', 2059400147),
        ('common-terminal-workflows-flashcards.html', 'CS Vocab::Common Terminal Workflows', 'cs-vocab-workflows.apkg', 2059400148),
        ('pytorch-basics-flashcards.html', 'CS Vocab::pythonML::PyTorch Basics', 'cs-vocab-pytorch-basics.apkg', 2059400149),
        ('training-loop-flashcards.html', 'CS Vocab::pythonML::Training Loop', 'cs-vocab-training-loop.apkg', 2059400150),
        ('reinforcement-learning-flashcards.html', 'CS Vocab::pythonML::Reinforcement Learning', 'cs-vocab-reinforcement-learning.apkg', 2059400151),
        ('nlp-transformers-flashcards.html', 'CS Vocab::pythonML::NLP & Transformers', 'cs-vocab-nlp-transformers.apkg', 2059400152),
        ('model-evaluation-metrics-flashcards.html', 'CS Vocab::pythonML::Model Evaluation & Metrics', 'cs-vocab-model-evaluation.apkg', 2059400153),
        ('advanced-pytorch-flashcards.html', 'CS Vocab::pythonML::Advanced PyTorch', 'cs-vocab-advanced-pytorch.apkg', 2059400154),
        ('mlops-langfuse-flashcards.html', 'CS Vocab::pythonML::MLOps with LangFuse', 'cs-vocab-mlops-langfuse.apkg', 2059400155),
        ('attention-mechanisms-flashcards.html', 'CS Vocab::pythonML::Attention Mechanisms', 'cs-vocab-attention.apkg', 2059400156),
        ('ffn-activations-flashcards.html', 'CS Vocab::pythonML::Feed-Forward Networks & Activations', 'cs-vocab-ffn.apkg', 2059400157),
        ('layer-norm-flashcards.html', 'CS Vocab::pythonML::Layer Normalization', 'cs-vocab-layer-norm.apkg', 2059400158),
        ('generation-strategies-flashcards.html', 'CS Vocab::pythonML::Generation Strategies', 'cs-vocab-generation.apkg', 2059400159),
        ('tokenization-flashcards.html', 'CS Vocab::pythonML::Tokenization', 'cs-vocab-tokenization.apkg', 2059400160),
        ('training-dynamics-flashcards.html', 'CS Vocab::pythonML::Training Dynamics', 'cs-vocab-training.apkg', 2059400161),
        ('inference-optimization-flashcards.html', 'CS Vocab::pythonML::Inference Optimization', 'cs-vocab-inference.apkg', 2059400162),
        ('loss-functions-flashcards.html', 'CS Vocab::pythonML::Loss Functions & Objectives', 'cs-vocab-loss-functions.apkg', 2059400163),
        ('peft-flashcards.html', 'CS Vocab::pythonML::Parameter-Efficient Fine-Tuning', 'cs-vocab-peft.apkg', 2059400164),
        ('transformer-variants-flashcards.html', 'CS Vocab::pythonML::Transformer Variants', 'cs-vocab-transformers.apkg', 2059400165),
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
    print('  - cs-vocab-find.apkg        (Find and Tree Commands only)')
    print('  - cs-vocab-package-diff.apkg (Package Management & Diff only)')
    print('  - cs-vocab-text.apkg        (Text Processing only)')
    print('  - cs-vocab-permissions.apkg (Permissions & Ownership only)')
    print('  - cs-vocab-archives.apkg    (Archives & Compression only)')
    print('  - cs-vocab-logs.apkg        (System Logs & Monitoring only)')
    print('  - cs-vocab-users.apkg       (User & Group Management only)')
    print('  - cs-vocab-disk.apkg        (Disk Management only)')
    print('  - cs-vocab-symlinks.apkg    (Symbolic Links & File Attributes only)')
    print('  - cs-vocab-xargs.apkg       (xargs & Command Chaining only)')
    print('  - cs-vocab-grep.apkg        (Grep Deep Dive only)')
    print('  - cs-vocab-gcloud.apkg      (GCloud ML Training only)')
    print('  - cs-vocab-vscode.apkg      (VSCode Productivity only)')
    print('  - cs-vocab-history.apkg     (Bash History & Command Recall only)')
    print('  - cs-vocab-job-control.apkg (Job Control only)')
    print('  - cs-vocab-redirection.apkg (Redirection & Pipes only)')
    print('  - cs-vocab-env-vars.apkg    (Environment Variables & PATH only)')
    print('  - cs-vocab-quoting.apkg     (Quoting & Escaping only)')
    print('  - cs-vocab-exit-status.apkg (Exit Status & Return Codes only)')
    print('  - cs-vocab-globbing.apkg    (Brace Expansion & Globbing only)')
    print('  - cs-vocab-functions.apkg   (Aliases, Functions & Scripts only)')
    print('  - cs-vocab-ci.apkg          (CI/Continuous Integration only)')
    print('  - cs-vocab-linux-history.apkg (Linux History & Trivia only)')
    print('  - cs-vocab-sed.apkg         (Sed Deep Dive only)')
    print('  - cs-vocab-sociopolitical.apkg (Linux Sociopolitical History only)')
    print('  - cs-vocab-common-errors.apkg (Common CLI Errors & Antipatterns only)')
    print('  - cs-vocab-workflows.apkg   (Common Terminal Workflows only)')
    print('  - cs-vocab-pytorch-basics.apkg (PyTorch Basics only)')
    print('  - cs-vocab-training-loop.apkg (PyTorch Training Loop only)')
    print('  - cs-vocab-reinforcement-learning.apkg (Reinforcement Learning only)')
    print('  - cs-vocab-nlp-transformers.apkg (NLP & Transformers only)')
    print('  - cs-vocab-model-evaluation.apkg (Model Evaluation & Metrics only)')
    print('  - cs-vocab-advanced-pytorch.apkg (Advanced PyTorch only)')
    print('  - cs-vocab-mlops-langfuse.apkg (MLOps with LangFuse only)')
    print('  - cs-vocab-attention.apkg   (Attention Mechanisms only)')
    print('  - cs-vocab-ffn.apkg         (Feed-Forward Networks & Activations only)')
    print('  - cs-vocab-layer-norm.apkg  (Layer Normalization only)')
    print('  - cs-vocab-generation.apkg  (Generation Strategies only)')
    print('  - cs-vocab-tokenization.apkg (Tokenization only)')
    print('  - cs-vocab-training.apkg    (Training Dynamics only)')
    print('  - cs-vocab-inference.apkg   (Inference Optimization only)')
    print('  - cs-vocab-loss-functions.apkg (Loss Functions & Objectives only)')
    print('  - cs-vocab-peft.apkg        (Parameter-Efficient Fine-Tuning only)')
    print('  - cs-vocab-transformers.apkg (Transformer Variants only)')
    print()
    print('Combined package:')
    print('  - cs-vocab-all.apkg         (All topics)')
    print()
    print('Import creates subdeck structure: CS Vocab → [56 subdecks]')
