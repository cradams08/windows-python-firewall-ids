import json

def load_rules(filename="rules.json"):
    with open(filename, "r") as f:
        return json.load(f)

def get_firewall_rules(rules):
    return rules.get("firewall_rules", [])

def get_ids_rules(rules):
    return rules.get("ids_rules", [])