import subprocess
import re
import sys

def get_ipv4():
    try:
        if sys.platform.startswith("win"):
            # Windows
            output = subprocess.check_output(
                ["ipconfig"],
                text=True,
                stderr=subprocess.DEVNULL
            )
            matches = re.findall(r"IPv4 Address[^\d]*([\d\.]+)", output)
        else:
            # Linux / macOS
            output = subprocess.check_output(
                ["ip", "-4", "addr"],
                text=True,
                stderr=subprocess.DEVNULL
            )
            matches = re.findall(r"inet (\d+\.\d+\.\d+\.\d+)", output)

        for ip in matches:
            if not ip.startswith("127."):
                return(ip)

        return("No IPv4 address found")

    except Exception as e:
        return("Failed to get IPv4 address:", e)
