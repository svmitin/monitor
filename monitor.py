from datetime import datetime
import time

import psutil


def save_snapshot() -> None:
    current_time = datetime.now()
    ram_usage_percent = psutil.virtual_memory().percent
    swap_usage_percent = psutil.swap_memory().percent
    disk_usage_percent = psutil.disk_usage('/')[3]

    proc_mem = []
    for p in psutil.process_iter(['name', 'memory_info']):
        if not p.info['memory_info']:
            continue
        name = p.info['name']
        mem = round(p.info['memory_info'].rss / 1024 / 1024, 2)
        if mem < 20:
            continue
        proc_mem.append((mem, name,))

    result = {
        'time': current_time.strftime('%Y-%m-%d %H:%M:%S'),
        'ram': ram_usage_percent,
        'swap': swap_usage_percent,
        'disk': disk_usage_percent,
        'procs': str(sorted(proc_mem, key=lambda p: p[0])[::-1][::10])
    }
    with open('memory.log', 'a') as f:
        f.write(str(result) + '\n')

while True:
    save_snapshot()
    time.sleep(1)
