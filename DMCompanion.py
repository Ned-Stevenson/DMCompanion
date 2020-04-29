from enum import auto, Enum
import Ui

if input("Do you want to use the GUI? y/n ").lower()[0] == "y":
    UI = Ui.GUI()
else:
    UI = Ui.Terminal()

def save():
    """Save character sheets and world progress before crashing from exception"""
    pass

def load():
    """Load a save"""
    pass

try:
    UI.run()
except Exception as e: #When exception is encountered, save before raising the exception
    save()
    raise e