from enum import auto, Enum
import Ui

if input("Do you want to use the GUI? y/n ").lower()[0] == "y":
    UI = Ui.GUI()
else:
    UI = Ui.Terminal()

def save():
    """Save character sheets and world progress before crashing from exception"""
    pass

try:
    UI.run()
except Exception as e:
    save()
    raise e