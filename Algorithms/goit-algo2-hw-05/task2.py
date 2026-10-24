import json
import time
from datasketch import HyperLogLogPlusPlus

LOG_FILE = "lms-stage-access.log"

def extract_ips(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            try:
                record = json.loads(line)
                ip = record.get("remote_addr")
                if ip:
                    yield ip
            except json.JSONDecodeError:
                continue  # Пропустити рядки з помилками

def exact_count(ip_list):
    start = time.time()
    unique_ips = set(ip_list)
    duration = time.time() - start
    return len(unique_ips), duration

def hllpp_count(ip_list, precision=14):
    hllpp = HyperLogLogPlusPlus(p=precision)
    start = time.time()
    for ip in ip_list:
        hllpp.update(ip.encode("utf-8"))
    duration = time.time() - start
    return int(hllpp.count()), duration

def main():
    ip_list = list(extract_ips(LOG_FILE))

    exact_result, exact_time = exact_count(ip_list)
    hllpp_result, hllpp_time = hllpp_count(ip_list)

    print("\nРезультати порівняння:")
    print(f"{'':<30}{'Точний підрахунок':>20}   {'HyperLogLog++':>12}")
    print(f"{'Унікальні елементи':<30}{exact_result:>20,.1f}   {hllpp_result:>12,.1f}")
    print(f"{'Час виконання (сек.)':<30}{exact_time:>20.2f}   {hllpp_time:>12.2f}")

if __name__ == "__main__":
    main()