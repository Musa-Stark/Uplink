import asyncio
import websockets
import json
import pyautogui
from cursor_movement import handle_mouse_move
from actions import windows_action
from scroll import handle_scroll
from get_ipv4 import get_ipv4
from stats import get_system_info

# exeception timeout

pyautogui.FAILSAFE = False

async def handler(ws):
    try:
        async for message in ws:
            data = json.loads(message)
            if "greetings" in data:
                print("✅ Connected!")

            elif "cmd" in data:
                if data["cmd"] == "stats":
                    await ws.send(json.dumps({"stats": get_system_info()}))
                else:
                    windows_action(data['cmd'])

            elif "x" in data and "y" in data:
                handle_mouse_move(data['x'], data['y'])
            
            elif "click" in data:
                pyautogui.click(button='left')

            elif "y" in data:
                handle_scroll(int(data["y"]))
            
            elif "text" in data:
                windows_action("type_text", text=data["text"])

    except asyncio.TimeoutError:
        print("⏱️ Connection timed out")

    except websockets.exceptions.ConnectionClosed:
        print("🔌 Client disconnected")

    except PermissionError as e:
        print(f"⛔ Permission error: {e}")

    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON received: {e}")

    except Exception as e:
        print(f"🔥 Unexpected handler error: {e}")


async def main():
    server = await websockets.serve(handler, "0.0.0.0", 8765)
    print("\n===========================")
    print(f"IP Address: {get_ipv4()}")
    print("===========================\n")
    print("Server running...")
    await server.wait_closed()

asyncio.run(main())
