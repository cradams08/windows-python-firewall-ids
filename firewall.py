import pydivert
from utils import load_rules, get_firewall_rules

def build_filter_expression(rule):
    exp = []
    if rule.get("direction"):
        exp.append(rule["direction"])
    if rule.get("protocol"):
        exp.append(rule["protocol"])
    if rule.get("dst_port"):
        exp.append(f"{rule['protocol']}.DstPort == {rule['dst_port']}")
    if rule.get("ip"):
        # Note: pydivert supports ip.SrcAddr/DstAddr matching
        exp.append(f"ip.SrcAddr == {rule['ip']}")
    return " and ".join(exp)

def run_firewall():
    rules = load_rules()
    for rule in get_firewall_rules(rules):
        if rule.get("action") == "block":
            expr = build_filter_expression(rule)
            print(f"Applying firewall rule: {rule['name']}")
            with pydivert.WinDivert(expr) as w:
                for packet in w:
                    # Drop matching packets (do not reinject)
                    print(f"Blocked: {packet}")

if __name__ == "__main__":
    run_firewall()
