# 🔗 Uplink

**Uplink** is a mobile-to-PC control system that turns your phone into a **wireless touchpad, keyboard, and system controller** for your laptop or desktop.

Built with:
- **React Native (Expo)** for the mobile client  
- **Python WebSocket server** for the target PC  

No cables. No bloated remote desktop software. Just fast, direct control.

---

## ✨ What Uplink Does

Uplink lets you control your computer from your phone in real time:

- Use your phone as a **touchpad**
- Perform **mouse clicks and gestures**
- Type text remotely as if using a real keyboard
- Trigger **system actions** like shutdown or restart
- View **live system stats** from your PC

---

## 🧩 Architecture

Uplink has **two parts**:

### 1️⃣ Mobile App (Client)
- Built with **React Native (Expo)**
- Runs on Android (APK provided)
- Connects to the PC via **WebSocket**
- Requires the **IP address of the target machine**

### 2️⃣ Python WebSocket Server
- Runs on the **target laptop / PC**
- Executes system-level actions
- Sends system information back to the client
- Displays the local IP address on startup

---

## 📱 Mobile App Features

### 🔹 Connection
- Input the **IP address of the laptop**
- Establishes a WebSocket connection
- Real-time communication with the PC

---

### 🏠 Home Tab
Primary control surface.

- Touchpad (mouse movement)
- Left Mouse Button (LMB)
- Right Mouse Button (RMB)
- Directional buttons:
  - Up
  - Down
  - Left
  - Right

---

### ⚡ Action Tab
Quick-access system and navigation controls.

Includes buttons for:
- Copy
- Paste
- Enter
- Backspace
- Scroll Up
- Scroll Down
- Arrow navigation (Up / Down / Left / Right)
- Desktop switching
- Shutdown
- Restart  
*(More actions can be added easily)*

---

### ⌨️ Keyboard Tab
Remote typing made simple.

- Auto-focused **text area**
- Type text on your phone
- Press **Send**
- Text is typed on the laptop **character by character** as real keyboard input

Perfect for:
- Presentations
- Media PCs
- Remote work
- Lazy setups 😌

---

### 📊 Stats Tab
Live system information from the connected PC.

Displays:
- Host name
- Operating system
- CPU usage
- RAM usage
- Battery status (if available)
- Other system metrics

Stats refresh **each time you open the tab**.

---

## 🖥️ Python WebSocket Server

The server runs on the target machine and handles all system interactions.

### 🔧 Libraries Used
- `pyautogui` – mouse and keyboard control
- `win32api / win32con` – Windows system interactions
- `psutil` – system stats (CPU, RAM, battery, etc.)
- `websockets` / `asyncio` – real-time communication

### 🖨️ On Startup
- Automatically fetches the local IP address
- Prints the IP to the console
- Waits for incoming mobile connections

---

## 🚀 How It Works (High Level)

1. Start the **Python server** on your PC
2. Server prints the local IP address
3. Open **Uplink mobile app**
4. Enter the IP address
5. Connect
6. Control your PC instantly

---

## 📦 Downloads & Source Code

- 📱 **APK (Android):** _[Link will be added]_
- 🖥️ **Python Server Code:** _[Link will be added]_

---

## 🔒 Notes & Limitations

- Server must be running on the PC
- Both devices must be on the **same network**
- Currently optimized for **Windows**
- Security/authentication not implemented (demo version)

---

## 🧠 Future Improvements

- Authentication / pairing
- macOS & Linux support
- Gesture-based actions
- File transfer
- Media controls
- Background server service
- Encrypted communication

---

## 📄 License

This project is for **learning, experimentation, and demos**.  
Feel free to fork, modify, and extend it.

---

## 👤 Author

Built by **Stark**  
If you’re reading this, you already know this wasn’t built by accident.
