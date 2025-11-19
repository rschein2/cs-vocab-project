"""
AI Assistant Dialog - Main UI for interacting with AI about cards
"""

from aqt.qt import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
                     QTextEdit, QComboBox, QGroupBox, QMessageBox, Qt)
from aqt.utils import showInfo, tooltip
from aqt import mw
import re
from .api_client import call_ai_api, estimate_tokens


class AIAssistantDialog(QDialog):
    """Dialog for AI-assisted card editing."""

    def __init__(self, parent, card):
        super().__init__(parent)
        self.card = card
        self.note = card.note()
        self.config = mw.addonManager.getConfig(__name__)

        self.setup_ui()
        self.load_card_content()

    def setup_ui(self):
        """Set up the dialog UI."""
        self.setWindowTitle("AI Card Assistant")
        self.setMinimumSize(700, 600)

        layout = QVBoxLayout()

        # Card content display
        card_group = QGroupBox("Current Card")
        card_layout = QVBoxLayout()

        self.front_display = QLabel()
        self.front_display.setWordWrap(True)
        self.front_display.setStyleSheet("padding: 10px; background: #f0f0f0; border-radius: 4px;")

        self.back_display = QLabel()
        self.back_display.setWordWrap(True)
        self.back_display.setStyleSheet("padding: 10px; background: #f0f0f0; border-radius: 4px;")

        card_layout.addWidget(QLabel("<b>Front:</b>"))
        card_layout.addWidget(self.front_display)
        card_layout.addWidget(QLabel("<b>Back:</b>"))
        card_layout.addWidget(self.back_display)
        card_group.setLayout(card_layout)
        layout.addWidget(card_group)

        # Action selection
        action_group = QGroupBox("What would you like to do?")
        action_layout = QVBoxLayout()

        self.action_combo = QComboBox()
        self.action_combo.addItems([
            "Ask a custom question",
            "Simplify the explanation",
            "Add a practical example",
            "Clarify a confusing part",
            "Create a related card",
            "Add mnemonics or memory aids",
            "Explain like I'm 5",
            "Add alternative explanations"
        ])
        self.action_combo.currentTextChanged.connect(self.on_action_changed)
        action_layout.addWidget(self.action_combo)

        # Custom question input
        self.question_label = QLabel("Your question:")
        self.question_input = QTextEdit()
        self.question_input.setMaximumHeight(80)
        self.question_input.setPlaceholderText("Ask anything about this card...")
        action_layout.addWidget(self.question_label)
        action_layout.addWidget(self.question_input)

        action_group.setLayout(action_layout)
        layout.addWidget(action_group)

        # Response area
        response_group = QGroupBox("AI Response")
        response_layout = QVBoxLayout()

        self.response_display = QTextEdit()
        self.response_display.setReadOnly(True)
        self.response_display.setPlaceholderText("AI response will appear here...")
        response_layout.addWidget(self.response_display)

        response_group.setLayout(response_layout)
        layout.addWidget(response_group)

        # Buttons
        button_layout = QHBoxLayout()

        self.cost_label = QLabel("Estimated cost: $0.00")
        self.cost_label.setStyleSheet("color: #666; font-size: 11px;")
        button_layout.addWidget(self.cost_label)

        button_layout.addStretch()

        self.ask_button = QPushButton("Ask AI")
        self.ask_button.clicked.connect(self.ask_ai)
        self.ask_button.setStyleSheet("""
            QPushButton {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background: linear-gradient(135deg, #5568d3 0%, #653a8b 100%);
            }
        """)
        button_layout.addWidget(self.ask_button)

        self.apply_button = QPushButton("Apply to Card")
        self.apply_button.clicked.connect(self.apply_changes)
        self.apply_button.setEnabled(False)
        button_layout.addWidget(self.apply_button)

        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.reject)
        button_layout.addWidget(self.close_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def load_card_content(self):
        """Load and display current card content."""
        # Get fields
        fields = self.note.fields
        model = self.note.model()

        # Usually first field is front, second is back
        if len(fields) >= 2:
            front = self.strip_html(fields[0])
            back = self.strip_html(fields[1])
        else:
            front = self.strip_html(fields[0]) if fields else "No content"
            back = "No content"

        self.front_display.setText(front[:200] + "..." if len(front) > 200 else front)
        self.back_display.setText(back[:300] + "..." if len(back) > 300 else back)

        # Store full content
        self.front_text = fields[0] if len(fields) > 0 else ""
        self.back_text = fields[1] if len(fields) > 1 else ""

    def strip_html(self, text):
        """Remove HTML tags for display."""
        return re.sub('<[^<]+?>', '', text).strip()

    def on_action_changed(self, action):
        """Handle action selection change."""
        if action == "Ask a custom question":
            self.question_label.show()
            self.question_input.show()
            self.question_input.clear()
        else:
            self.question_label.hide()
            self.question_input.hide()

    def build_prompt(self):
        """Build the prompt to send to AI."""
        action = self.action_combo.currentText()

        # Strip HTML for cleaner prompt
        front_clean = self.strip_html(self.front_text)
        back_clean = self.strip_html(self.back_text)

        # Get deck and tags for context
        deck_name = mw.col.decks.name(self.card.did)
        tags = " ".join(self.note.tags)

        base_context = f"""I'm studying a flashcard from the deck "{deck_name}".

Card Front: {front_clean}

Card Back: {back_clean}

Tags: {tags}
"""

        if action == "Ask a custom question":
            user_question = self.question_input.toPlainText().strip()
            if not user_question:
                return None
            prompt = base_context + f"\nMy question: {user_question}\n\nPlease help me with this question about the card."

        elif action == "Simplify the explanation":
            prompt = base_context + "\nPlease rewrite the back of this card in simpler, more accessible language while keeping all the key information."

        elif action == "Add a practical example":
            prompt = base_context + "\nPlease provide a practical, real-world example that illustrates this concept. Format it so I can add it to the card."

        elif action == "Clarify a confusing part":
            prompt = base_context + "\nPlease identify any potentially confusing parts of this explanation and clarify them. If everything is clear, suggest ways to make it even clearer."

        elif action == "Create a related card":
            prompt = base_context + "\nPlease suggest a related flashcard that would complement this one. Provide both the front (question) and back (answer) for a new card."

        elif action == "Add mnemonics or memory aids":
            prompt = base_context + "\nPlease create a mnemonic, memory aid, or mental association to help remember this information."

        elif action == "Explain like I'm 5":
            prompt = base_context + "\nPlease explain this concept in very simple terms, as if teaching it to a young child. Use analogies and simple language."

        elif action == "Add alternative explanations":
            prompt = base_context + "\nPlease provide an alternative way to understand or explain this concept. Different perspectives help learning."

        return prompt

    def ask_ai(self):
        """Send request to AI."""
        # Build prompt
        prompt = self.build_prompt()
        if not prompt:
            showInfo("Please enter a question.")
            return

        # Check API key
        if not self.config.get("api_key"):
            QMessageBox.warning(
                self,
                "API Key Required",
                "Please set up your API key in Tools → AI Assistant Settings first.\n\n"
                "Get your key at: https://console.anthropic.com"
            )
            return

        # Estimate cost
        tokens = estimate_tokens(prompt)
        cost = tokens * 0.000003  # Approximate cost
        self.cost_label.setText(f"Estimated cost: ${cost:.4f}")

        # Disable button
        self.ask_button.setEnabled(False)
        self.ask_button.setText("Thinking...")

        try:
            # Call API
            response = call_ai_api(
                prompt,
                self.config.get("api_key"),
                self.config.get("model", "claude-sonnet-4-20250514"),
                self.config.get("max_tokens", 1024)
            )

            # Display response
            self.response_display.setPlainText(response)
            self.apply_button.setEnabled(True)

            tooltip("Response received!", 2000)

        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Failed to get AI response:\n\n{str(e)}\n\n"
                "Please check your API key and internet connection."
            )
            self.response_display.setPlainText(f"Error: {str(e)}")

        finally:
            self.ask_button.setEnabled(True)
            self.ask_button.setText("Ask AI")

    def apply_changes(self):
        """Apply AI suggestions to card."""
        action = self.action_combo.currentText()
        response = self.response_display.toPlainText()

        if not response:
            return

        # Ask for confirmation
        reply = QMessageBox.question(
            self,
            "Apply Changes",
            "How would you like to apply this?\n\n"
            "Yes: Replace card content\n"
            "No: Append to card\n"
            "Cancel: Don't apply",
            QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel
        )

        if reply == QMessageBox.Cancel:
            return

        # Handle different actions
        if action == "Create a related card":
            self.create_new_card(response)
        else:
            self.modify_current_card(response, append=(reply == QMessageBox.No))

    def modify_current_card(self, content, append=False):
        """Modify the current card."""
        # Update back field (index 1)
        if len(self.note.fields) > 1:
            if append:
                self.note.fields[1] = self.back_text + "\n\n<hr>\n\n" + content
            else:
                self.note.fields[1] = content

            # Save
            self.note.flush()
            mw.col.reset()

            # Update display
            self.load_card_content()

            tooltip("Card updated!", 2000)
            showInfo("Card has been updated. The changes will appear on next review.")

    def create_new_card(self, content):
        """Create a new related card."""
        # Try to parse front and back from response
        lines = content.split('\n')

        front = ""
        back = ""
        capture_front = False
        capture_back = False

        for line in lines:
            line_lower = line.lower().strip()
            if 'front' in line_lower or 'question' in line_lower:
                capture_front = True
                capture_back = False
                continue
            elif 'back' in line_lower or 'answer' in line_lower:
                capture_back = True
                capture_front = False
                continue

            if capture_front and line.strip():
                front += line + "\n"
            elif capture_back and line.strip():
                back += line + "\n"

        if not front or not back:
            # Couldn't parse, show full response
            showInfo(f"Please create this card manually:\n\n{content[:500]}")
            return

        # Create new note with same model
        new_note = mw.col.newNote()
        new_note.fields[0] = front.strip()
        if len(new_note.fields) > 1:
            new_note.fields[1] = back.strip()

        # Copy tags and add ai-generated
        new_note.tags = self.note.tags.copy()
        if self.config.get("auto_tag_ai_cards", True):
            new_note.tags.append("ai-generated")

        # Add to collection
        mw.col.addNote(new_note)
        mw.col.reset()

        tooltip("New card created!", 2000)
        showInfo(f"New related card created!\n\nFront: {front[:100]}...")
