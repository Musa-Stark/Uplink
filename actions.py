import subprocess
import pyautogui
import ctypes
import time
import os

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.05


# =========================
# SYSTEM LEVEL (REAL APIs)
# =========================

def lock():
    ctypes.windll.user32.LockWorkStation()


def sleep():
    subprocess.run(
        ["rundll32.exe", "powrprof.dll,SetSuspendState", "0,1,0"],
        shell=True
    )


def shutdown():
    subprocess.run("shutdown /s /t 0", shell=True)


def restart():
    subprocess.run("shutdown /r /t 0", shell=True)


def sign_out():
    subprocess.run("shutdown /l", shell=True)


# =========================
# APPLICATIONS
# =========================

def open_app(app):
    subprocess.Popen(app, shell=True)


def open_url(url):
    subprocess.Popen(f'start "" "{url}"', shell=True)


def task_manager():
    pyautogui.hotkey("ctrl", "shift", "esc")


def close_active():
    pyautogui.hotkey("alt", "f4")


# =========================
# DESKTOP / WINDOWS
# =========================

def show_desktop():
    pyautogui.hotkey("win", "d")


def task_view():
    pyautogui.hotkey("win", "tab")


def switch_desktop(direction):
    pyautogui.hotkey("ctrl", "win", direction)


def snap(direction):
    pyautogui.hotkey("win", direction)


def move_window_monitor(direction):
    pyautogui.hotkey("win", "shift", direction)


# =========================
# VOLUME / MEDIA
# =========================

def volume_up():
    pyautogui.press("volumeup")


def volume_down():
    pyautogui.press("volumedown")


def mute():
    pyautogui.press("volumemute")


def media_play_pause():
    pyautogui.press("playpause")


def media_next():
    pyautogui.press("nexttrack")


def media_prev():
    pyautogui.press("prevtrack")


# =========================
# FILE EXPLORER
# =========================

def open_explorer():
    pyautogui.hotkey("win", "e")


def new_folder():
    pyautogui.hotkey("ctrl", "shift", "n")


def rename():
    pyautogui.press("f2")


def explorer_up():
    pyautogui.hotkey("alt", "up")

def copy():
    pyautogui.hotkey("ctrl", "c")

def paste():
    pyautogui.hotkey("ctrl", "v")


# =========================
# INPUT CONTROL
# =========================

def click(button="left"):
    pyautogui.click(button=button)

def double_click():
    pyautogui.doubleClick()


def right_click():
    pyautogui.click(button="right")


def type_text(text):
    pyautogui.write(text, interval=0.03)


def press(key):
    pyautogui.press(key)


def hotkey(*keys):
    pyautogui.hotkey(*keys)

# =========================
# SCREEN / DISPLAY
# =========================

def screenshot(path="screenshot.png"):
    pyautogui.screenshot(path)


def snip():
    pyautogui.hotkey("win", "shift", "s")


def project_mode():
    pyautogui.hotkey("win", "p")

def scroll_up():
    pyautogui.scroll(300)

def scroll_down():
    pyautogui.scroll(-300)

def move(direction):
    pyautogui.press(direction)

# =========================
# MASTER ROUTER
# =========================

def windows_action(action, **kwargs):
    """
    Single Windows command router.
    """

    actions = {

        # --- SYSTEM ---
        "lock": lock,
        "sleep": sleep,
        "shutdown": shutdown,
        "restart": restart,
        "sign_out": sign_out,

        # --- APPS ---
        "open_app": lambda: open_app(kwargs.get("app")),
        "open_url": lambda: open_url(kwargs.get("url")),
        "task_manager": task_manager,
        "close": close_active,

        # --- DESKTOP ---
        "show_desktop": show_desktop,
        "task_view": task_view,
        "desktop_left": lambda: switch_desktop("left"),
        "desktop_right": lambda: switch_desktop("right"),
        "snap_left": lambda: snap("left"),
        "snap_right": lambda: snap("right"),
        "snap_up": lambda: snap("up"),
        "snap_down": lambda: snap("down"),
        "move_monitor_left": lambda: move_window_monitor("left"),
        "move_monitor_right": lambda: move_window_monitor("right"),

        # --- VOLUME ---
        "volume_up": volume_up,
        "volume_down": volume_down,
        "mute": mute,
        "play_pause": media_play_pause,
        "next_track": media_next,
        "prev_track": media_prev,

        # --- FILES ---
        "explorer": open_explorer,
        "new_folder": new_folder,
        "rename": rename,
        "explorer_up": explorer_up,
        "copy": copy,
        "paste": paste,

        # --- INPUT ---
        "click": click,
        "LMB": click,
        "double_click": double_click,
        "RMB": right_click,
        "right_click": right_click,
        "type": lambda: type_text(kwargs.get("text", "")),
        "press": lambda: press(kwargs.get("key")),
        "hotkey": lambda: hotkey(*kwargs.get("keys", [])),
        "enter": lambda: press("enter"),
        "backspace": lambda: press("backspace"),
        "type_text": lambda: type_text(kwargs.get("text", "")),

        # --- SCREEN ---
        "screenshot": lambda: screenshot(f"screenshots/{time.time()}.png"),
        "snip": snip,
        "project": project_mode,
        "scroll_up": scroll_up,
        "scroll_down": scroll_down,
        "up": lambda: move("up"),
        "down": lambda: move("down"),
        "left": lambda: move("left"),
        "right": lambda: move("right"),
    }

    if action not in actions:
        raise ValueError(f"Unknown action: {action}")

    actions[action]()
