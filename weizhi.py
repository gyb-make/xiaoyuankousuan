import keyboard
import pyautogui

keyboard.add_hotkey('space', lambda: print(pyautogui.position()))
keyboard.wait()
