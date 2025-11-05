from scapy.all import sniff, IP, TCP, Raw
from utils import load_rules, get_ids_rules

def packet_callback(pkt, ids_rules):
    for rule in ids_rules:
        # Check protocol and port
        if rule.get("protocol") == "tcp" and TCP in pkt:
            if rule.get("dst_port") and pkt[TCP].dport == rule["dst_port"]:
                print(f"ALERT: {rule['alert']} from {pkt[IP].src}")
        # Payload signature detection
        if "payload_pattern" in rule and Raw in pkt and rule["payload_pattern"].encode() in pkt[Raw].load:
            print(f"ALERT: {rule['alert']} from {pkt[IP].src}")

def run_ids():
    rules = load_rules()
    ids_rules = get_ids_rules(rules)
    print("IDS running: monitoring traffic...")
    sniff(filter="tcp", prn=lambda pkt: packet_callback(pkt, ids_rules), store=0)

if __name__ == "__main__":
    run_ids()