import ctypes
from ctypes import wintypes

user32 = ctypes.WinDLL("user32", use_last_error=True)

# Input constants
INPUT_MOUSE = 0
MOUSEEVENTF_WHEEL = 0x0800
WHEEL_DELTA = 120  # Windows standard

# ULONG_PTR fix for 32/64-bit
if hasattr(wintypes, "ULONG_PTR"):
    ULONG_PTR = wintypes.ULONG_PTR
else:
    ULONG_PTR = ctypes.c_uint64 if ctypes.sizeof(ctypes.c_void_p) == 8 else ctypes.c_uint32

# Structures
class MOUSEINPUT(ctypes.Structure):
    _fields_ = (
        ("dx", wintypes.LONG),
        ("dy", wintypes.LONG),
        ("mouseData", wintypes.DWORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ULONG_PTR),
    )

class INPUT(ctypes.Structure):
    _fields_ = (
        ("type", wintypes.DWORD),
        ("mi", MOUSEINPUT),
    )

# ===============================
# Smooth scroll handler
# ===============================
SCROLL_SENSITIVITY = 0.0025  # tune this
scroll_buffer = 0.0

def handle_scroll(delta_y):
    """
    delta_y: float from JS gesture (positive = scroll down, negative = scroll up)
    Sends immediate scroll event via Windows SendInput.
    """
    global scroll_buffer
    scroll_buffer += -delta_y * SCROLL_SENSITIVITY

    # Convert buffer to integer wheel ticks
    scroll_amount = int(scroll_buffer)
    if scroll_amount != 0:
        inp = INPUT(
            type=INPUT_MOUSE,
            mi=MOUSEINPUT(
                dx=0,
                dy=0,
                mouseData=WHEEL_DELTA * scroll_amount,
                dwFlags=MOUSEEVENTF_WHEEL,
                time=0,
                dwExtraInfo=0,
            ),
        )
        sent = user32.SendInput(1, ctypes.byref(inp), ctypes.sizeof(INPUT))
        if sent != 1:
            raise ctypes.WinError(ctypes.get_last_error())

        # Remove the sent portion from buffer
        scroll_buffer -= scroll_amount
