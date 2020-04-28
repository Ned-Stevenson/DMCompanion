from enum import auto, Enum
import Ui

if input("Do you want to use the GUI? y/n ").lower()[0] == "y":
    UI = Ui.GUI()
else:
    UI = Ui.Terminal()

UI.run()