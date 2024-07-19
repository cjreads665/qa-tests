import psutil
import logging

CPU_LIMIT = 80
MEMORY_LIMIT = 80
DISK_LIMIT = 80


logging.basicConfig(level=logging.INFO)

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_LIMIT:
        logging.info("CPU going over 80%")
    return cpu_usage

def check_mem_usage():
    mem_usage = psutil.virtual_memory().percent
    if mem_usage > MEMORY_LIMIT:
        logging.info("virtual memory going over 80%")
    return mem_usage

def check_disk_usage():
    disk_usage = psutil.disk_usage("/").percent
    if disk_usage > DISK_LIMIT:
        logging.info("disk usage going over 80%")
    return disk_usage

def check_running_processes():
    processes = [p.info for p in psutil.process_iter(['pid','name'])]
    logging.info(f"running processes: {processes}")
    return processes

if __name__ == "__main__":
    check_cpu_usage()
    check_disk_usage()
    check_mem_usage()
    check_running_processes()
        