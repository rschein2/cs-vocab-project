"""
AI Card Assistant - Anki Add-on
Helps you refine, clarify, and expand flashcards using AI during review.
"""

from aqt import mw, gui_hooks
from aqt.qt import QAction, QKeySequence
from aqt.utils import showInfo, tooltip
from .ai_assistant import AIAssistantDialog
from .settings import open_settings


def on_ask_ai():
    """Open AI assistant dialog when user clicks button or presses shortcut."""
    # Check if we're in review mode
    if not mw.reviewer or not mw.reviewer.card:
        showInfo("Please open a card in review mode first.")
        return

    # Get current card
    card = mw.reviewer.card

    # Open AI assistant dialog
    dialog = AIAssistantDialog(mw, card)
    dialog.exec()


def setup_menu():
    """Add menu items to Anki's Tools menu."""
    # AI Assistant action
    action = QAction("Ask AI About Card", mw)
    action.setShortcut(QKeySequence("Ctrl+Shift+A"))
    action.triggered.connect(on_ask_ai)
    mw.form.menuTools.addAction(action)

    # Settings action
    settings_action = QAction("AI Assistant Settings", mw)
    settings_action.triggered.connect(open_settings)
    mw.form.menuTools.addAction(settings_action)


def add_reviewer_button(buttons, reviewer):
    """Add 'Ask AI' button to reviewer screen."""
    button = reviewer.bottom.web.eval(
        """
        (() => {
            const btn = document.createElement('button');
            btn.innerHTML = '🤖 Ask AI';
            btn.style.cssText = `
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 6px;
                font-size: 14px;
                font-weight: 600;
                cursor: pointer;
                margin: 5px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.2);
                transition: transform 0.2s;
            `;
            btn.onmouseover = () => btn.style.transform = 'scale(1.05)';
            btn.onmouseout = () => btn.style.transform = 'scale(1)';
            btn.onclick = () => pycmd('ai_assistant');
            return btn.outerHTML;
        })()
        """
    )
    return buttons + [("🤖", "ai_assistant")]


def handle_reviewer_shortcuts(handled, shortcuts):
    """Add keyboard shortcut for AI assistant."""
    shortcuts.append(("Ctrl+Shift+A", lambda: on_ask_ai()))


# Initialize add-on
def init():
    """Initialize the add-on."""
    # Add menu items
    setup_menu()

    # Add button to reviewer
    gui_hooks.reviewer_will_init_answer_buttons.append(add_reviewer_button)

    # Show welcome message on first run
    config = mw.addonManager.getConfig(__name__)
    if not config or not config.get("api_key"):
        tooltip("AI Card Assistant installed! Set up your API key in Tools → AI Assistant Settings", 5000)


# Run initialization
init()
