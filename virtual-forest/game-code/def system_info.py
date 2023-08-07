import psutil
from datetime import datetime

def system_info():
    # Get current date and time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Get network uptime
    network_uptime = psutil.net_if_stats()['lo'].uptime

    # Get IP address
    ip_address = psutil.net_if_addrs()['lo'][0].address

    # Get free RAM in bytes
    free_ram = psutil.virtual_memory().available

    # Convert free RAM to human-readable format
    def convert_bytes(size, unit=None):
        units = {'B': 0, 'KB': 1e3, 'MB': 1e6, 'GB': 1e9, 'TB': 1e12}
        if unit and unit.upper() in units:
            return size / units[unit.upper()]
        for unit in ['TB', 'GB', 'MB', 'KB', 'B']:
            if size >= units[unit]:
                return f"{size / units[unit]:.2f} {unit}"

    free_ram_readable = convert_bytes(free_ram, 'GB')

    return {
        "Date and Time": current_time,
        "Network Uptime (seconds)": network_uptime,
        "IP Address": ip_address,
        "Free RAM": free_ram_readable
    }
