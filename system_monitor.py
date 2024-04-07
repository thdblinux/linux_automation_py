import psutil
def monitor_system_resources():
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/')

    print(f'CPU Usage: {cpu_percent}%')
    print(f'Memory Usage: {memory_percent}%')
    print(f'Disk Usage: {disk_usage.used / (1024 * 1024 * 1024):.2f} GB used / {disk_usage.total / (1024 * 1024 * 1024):.2f} GB total')

monitor_system_resources()