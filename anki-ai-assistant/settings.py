"""
Settings dialog for AI Card Assistant
"""

from aqt.qt import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
                     QLineEdit, QComboBox, QGroupBox, QCheckBox, QSpinBox,
                     QMessageBox, Qt)
from aqt.utils import showInfo, tooltip
from aqt import mw
from .api_client import test_api_key


class SettingsDialog(QDialog):
    """Settings dialog for configuring AI assistant."""

    def __init__(self, parent):
        super().__init__(parent)
        self.config = mw.addonManager.getConfig(__name__)
        self.setup_ui()
        self.load_settings()

    def setup_ui(self):
        """Set up the settings UI."""
        self.setWindowTitle("AI Assistant Settings")
        self.setMinimumWidth(600)

        layout = QVBoxLayout()

        # API Configuration
        api_group = QGroupBox("API Configuration")
        api_layout = QVBoxLayout()

        # API Provider
        provider_layout = QHBoxLayout()
        provider_layout.addWidget(QLabel("Provider:"))
        self.provider_combo = QComboBox()
        self.provider_combo.addItems(["Anthropic Claude"])
        self.provider_combo.setEnabled(False)  # Only Claude for now
        provider_layout.addWidget(self.provider_combo)
        api_layout.addLayout(provider_layout)

        # API Key
        key_layout = QHBoxLayout()
        key_layout.addWidget(QLabel("API Key:"))
        self.api_key_input = QLineEdit()
        self.api_key_input.setEchoMode(QLineEdit.Password)
        self.api_key_input.setPlaceholderText("sk-ant-...")
        key_layout.addWidget(self.api_key_input)

        self.show_key_btn = QPushButton("👁")
        self.show_key_btn.setMaximumWidth(40)
        self.show_key_btn.setCheckable(True)
        self.show_key_btn.toggled.connect(self.toggle_key_visibility)
        key_layout.addWidget(self.show_key_btn)

        api_layout.addLayout(key_layout)

        # Get API Key link
        help_label = QLabel(
            '<a href="https://console.anthropic.com">Get your API key at console.anthropic.com</a>'
        )
        help_label.setOpenExternalLinks(True)
        help_label.setStyleSheet("color: #667eea; margin: 5px 0;")
        api_layout.addWidget(help_label)

        # Test button
        test_layout = QHBoxLayout()
        test_layout.addStretch()
        self.test_btn = QPushButton("Test API Key")
        self.test_btn.clicked.connect(self.test_api_key)
        test_layout.addWidget(self.test_btn)
        api_layout.addLayout(test_layout)

        api_group.setLayout(api_layout)
        layout.addWidget(api_group)

        # Model Configuration
        model_group = QGroupBox("Model Configuration")
        model_layout = QVBoxLayout()

        # Model selection
        model_select_layout = QHBoxLayout()
        model_select_layout.addWidget(QLabel("Model:"))
        self.model_combo = QComboBox()
        self.model_combo.addItems([
            "claude-sonnet-4-20250514",
            "claude-3-5-sonnet-20241022",
            "claude-3-opus-20240229"
        ])
        model_select_layout.addWidget(self.model_combo)
        model_layout.addLayout(model_select_layout)

        # Max tokens
        tokens_layout = QHBoxLayout()
        tokens_layout.addWidget(QLabel("Max Response Tokens:"))
        self.max_tokens_spin = QSpinBox()
        self.max_tokens_spin.setRange(256, 4096)
        self.max_tokens_spin.setValue(1024)
        self.max_tokens_spin.setSingleStep(256)
        tokens_layout.addWidget(self.max_tokens_spin)
        tokens_layout.addWidget(QLabel("(More tokens = longer responses, higher cost)"))
        tokens_layout.addStretch()
        model_layout.addLayout(tokens_layout)

        model_group.setLayout(model_layout)
        layout.addWidget(model_group)

        # Additional Options
        options_group = QGroupBox("Options")
        options_layout = QVBoxLayout()

        self.show_cost_checkbox = QCheckBox("Show cost estimates")
        self.show_cost_checkbox.setChecked(True)
        options_layout.addWidget(self.show_cost_checkbox)

        self.auto_tag_checkbox = QCheckBox("Auto-tag AI-generated cards with 'ai-generated'")
        self.auto_tag_checkbox.setChecked(True)
        options_layout.addWidget(self.auto_tag_checkbox)

        options_group.setLayout(options_layout)
        layout.addWidget(options_group)

        # Cost Information
        cost_group = QGroupBox("💰 Cost Information")
        cost_layout = QVBoxLayout()

        cost_info = QLabel(
            "<b>Approximate costs per query:</b><br>"
            "• Claude Sonnet 4: ~$0.003 - $0.008<br>"
            "• Claude 3.5 Sonnet: ~$0.003 - $0.015<br>"
            "• Claude 3 Opus: ~$0.015 - $0.075<br><br>"
            "<i>Costs vary based on prompt length and response length.<br>"
            "Typical usage: $0.50 - $2.00 per month for regular study.</i>"
        )
        cost_info.setWordWrap(True)
        cost_info.setStyleSheet("padding: 10px; background: #f9f9f9; border-radius: 4px;")
        cost_layout.addWidget(cost_info)

        cost_group.setLayout(cost_layout)
        layout.addWidget(cost_group)

        # Buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()

        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.save_settings)
        save_btn.setStyleSheet("""
            QPushButton {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border: none;
                padding: 8px 20px;
                border-radius: 6px;
                font-weight: bold;
            }
        """)
        button_layout.addWidget(save_btn)

        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(cancel_btn)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def load_settings(self):
        """Load current settings."""
        self.api_key_input.setText(self.config.get("api_key", ""))
        self.model_combo.setCurrentText(self.config.get("model", "claude-sonnet-4-20250514"))
        self.max_tokens_spin.setValue(self.config.get("max_tokens", 1024))
        self.show_cost_checkbox.setChecked(self.config.get("show_cost_estimate", True))
        self.auto_tag_checkbox.setChecked(self.config.get("auto_tag_ai_cards", True))

    def toggle_key_visibility(self, checked):
        """Toggle API key visibility."""
        if checked:
            self.api_key_input.setEchoMode(QLineEdit.Normal)
        else:
            self.api_key_input.setEchoMode(QLineEdit.Password)

    def test_api_key(self):
        """Test the API key."""
        api_key = self.api_key_input.text().strip()

        if not api_key:
            QMessageBox.warning(self, "No API Key", "Please enter an API key first.")
            return

        self.test_btn.setEnabled(False)
        self.test_btn.setText("Testing...")

        try:
            success, message = test_api_key(api_key, self.model_combo.currentText())

            if success:
                QMessageBox.information(
                    self,
                    "Success! ✓",
                    f"{message}\n\nYour API key is working correctly."
                )
            else:
                QMessageBox.warning(
                    self,
                    "API Key Test Failed",
                    f"Failed to connect:\n\n{message}\n\n"
                    "Please check your API key and try again."
                )

        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Error testing API key:\n\n{str(e)}"
            )

        finally:
            self.test_btn.setEnabled(True)
            self.test_btn.setText("Test API Key")

    def save_settings(self):
        """Save settings."""
        api_key = self.api_key_input.text().strip()

        if not api_key:
            reply = QMessageBox.question(
                self,
                "No API Key",
                "You haven't entered an API key. The add-on won't work without one.\n\n"
                "Save anyway?",
                QMessageBox.Yes | QMessageBox.No
            )
            if reply == QMessageBox.No:
                return

        # Update config
        self.config["api_key"] = api_key
        self.config["api_provider"] = "anthropic"
        self.config["model"] = self.model_combo.currentText()
        self.config["max_tokens"] = self.max_tokens_spin.value()
        self.config["show_cost_estimate"] = self.show_cost_checkbox.isChecked()
        self.config["auto_tag_ai_cards"] = self.auto_tag_checkbox.isChecked()

        # Save to disk
        mw.addonManager.writeConfig(__name__, self.config)

        tooltip("Settings saved!", 2000)
        self.accept()


def open_settings():
    """Open settings dialog."""
    dialog = SettingsDialog(mw)
    dialog.exec()
