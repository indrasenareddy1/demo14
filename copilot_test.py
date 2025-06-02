import os
import platform

def get_uptime():
    if platform.system() == "Windows":
        # Windows does not have /proc/uptime, use 'net stats srv'
        import subprocess
        output = subprocess.check_output("net stats srv", shell=True, text=True)
        for line in output.splitlines():
            if "Statistics since" in line:
                print(f"System uptime (since): {line}")
                return
        print("Could not determine uptime on Windows.")
    else:
        # Unix/Linux
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            uptime_hours = uptime_seconds // 3600
            uptime_minutes = (uptime_seconds % 3600) // 60
            print(f"System uptime: {int(uptime_hours)} hours {int(uptime_minutes)} minutes")

if __name__ == "__main__":
    get_uptime()
