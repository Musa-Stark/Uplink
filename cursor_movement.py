import ctypes
from ctypes import wintypes

# ===============================
# Windows SendInput setup
# ===============================

user32 = ctypes.WinDLL("user32", use_last_error=True)

INPUT_MOUSE = 0
MOUSEEVENTF_MOVE = 0x0001

# Handle missing ULONG_PTR in some Python versions
if hasattr(wintypes, "ULONG_PTR"):
    ULONG_PTR = wintypes.ULONG_PTR
else:
    ULONG_PTR = ctypes.c_uint64 if ctypes.sizeof(ctypes.c_void_p) == 8 else ctypes.c_uint32


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
# Mouse movement handler
# ===============================

# Sensitivity multiplier (tune this)
SENSITIVITY = 1.0


# handleMouseMove
def handle_mouse_move(dx, dy):
    """
    Fast, raw relative mouse movement using Windows SendInput.
    dx, dy are relative deltas (like a touchpad).
    """

    # Scale + clamp to int (SendInput requires integers)
    dx = int(dx * SENSITIVITY)
    dy = int(dy * SENSITIVITY)

    if dx == 0 and dy == 0:
        return

    inp = INPUT(
        type=INPUT_MOUSE,
        mi=MOUSEINPUT(
            dx=dx,
            dy=dy,
            mouseData=0,
            dwFlags=MOUSEEVENTF_MOVE,
            time=0,
            dwExtraInfo=0,
        ),
    )

    sent = user32.SendInput(1, ctypes.byref(inp), ctypes.sizeof(INPUT))
    if sent != 1:
        raise ctypes.WinError(ctypes.get_last_error())
