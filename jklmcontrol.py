# JKLM.FUN Controlling Module
# ---------------------------
# This requires the PyAutoGui
# and Keyboard modules to work.

# Made by Kareem from Syria.
try:
    import pyautogui
    import keyboard
except ImportError:
    raise ImportError("Oops! Sorry, but we seem to have not found either the PyAutoGui or Keyboard module or both. Please download either or both of these modules to continue.")

__all__ = ["chat", "set_greet", "send_greet", "info"]
greet = "Hello!"

def chat(contents):
    "Chats in JKLM.FUN."
    pyautogui.click(1140, 690)
    keyboard.write(contents)
    keyboard.press_and_release("enter")

def set_greet(greeting):
    "Sets current greeting."
    greet = greeting

def send_greet():
    "Sends current greeting in chat."
    chat(greet)

def info():
    "Information about this module."
    print("JKLM.FUN Controlling Module")
    print("---------------------------")
    print("Made by Kareem from Syria.")
    print("Welcome to JKLM.FUN Control!")
