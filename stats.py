import psutil
import platform
import socket
import time

def get_system_info():
    return {
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "os_version": platform.version(),
        "cpu_percent": psutil.cpu_percent(interval=0.5),
        "cpu_cores": psutil.cpu_count(),
        "memory": {
            "total": psutil.virtual_memory().total,
            "used": psutil.virtual_memory().used,
            "percent": psutil.virtual_memory().percent,
        },
        "disk": {
            "total": psutil.disk_usage("/").total,
            "used": psutil.disk_usage("/").used,
            "percent": psutil.disk_usage("/").percent,
        },
        "battery": {
            "percent": psutil.sensors_battery().percent if psutil.sensors_battery() else None,
            "plugged": psutil.sensors_battery().power_plugged if psutil.sensors_battery() else None,
        },
        "network": {
            "sent": psutil.net_io_counters().bytes_sent,
            "recv": psutil.net_io_counters().bytes_recv,
        },
        "timestamp": time.time(),
    }
