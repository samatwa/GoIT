from collections import Counter


def get_count_visits_from_ip(ips):
    ip_counts=Counter(ips)
    return ip_counts

def get_frequent_visit_from_ip(ips):
    ip_counts=get_count_visits_from_ip(ips)
    most_common=ip_counts.most_common(1)
    for i in most_common:
        return i
        