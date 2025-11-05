# Windows Python Firewall and Intrusion Detection System (IDS)

A simple, customizable Firewall and IDS for Windows using Python.  
Blocks unwanted traffic and alerts on suspicious activity based on rules you define in `rules.json`.

---

## Features

- **Custom Firewall Rules**: Block/allow traffic by protocol, port, direction, or IP.
- **Intrusion Detection**: Signature-based packet analysis; alerts for suspicious patterns, ports, or payloads.
- **Easy Rule Management**: Edit `rules.json` to adjust firewall/IDS behavior without touching code.
- **Extensible Architecture**: Clean file structure for rapid extension, e.g., advanced detection, logging, or GUI.

---

## Requirements

- **Windows 10/11 (Administrator Privileges required)**
- **Python 3.8+**
- [pydivert](https://pypi.org/project/pydivert/)
- [scapy](https://pypi.org/project/scapy/)
- [Npcap](https://npcap.com/) (for packet sniffing)

Install Python packages:
```sh
pip install pydivert scapy
```

---

## Setup

1. **Clone this repo**  
   ```sh
   git clone https://github.com/YOUR_USERNAME/windows-python-firewall-ids.git
   cd windows-python-firewall-ids
   ```

2. **Edit Rules**

   Update `rules.json` to suit your security needs:
   - `firewall_rules`: Block or allow traffic by criteria.
   - `ids_rules`: Define detection for ports, payload patterns, etc.

3. **Run the Project**  
   (Administrator privileges required)
   ```sh
   python main.py
   ```

---

## File Structure

```
firewall_ids/
├── main.py           # Orchestrates Firewall & IDS
├── firewall.py       # Loads firewall rules, applies packet filtering
├── ids.py            # Loads IDS rules, sniffs and analyzes traffic
├── utils.py          # Rule loader & helpers
├── rules.json        # Your customizable firewall/IDS rule definitions
├── README.md         # This documentation
```

---

## Sample `rules.json`

```json
{
  "firewall_rules": [
    {"name": "Block outbound HTTP", "direction": "outbound", "protocol": "tcp", "dst_port": 80, "action": "block"},
    {"name": "Allow DNS", "direction": "outbound", "protocol": "udp", "dst_port": 53, "action": "allow"}
  ],
  "ids_rules": [
    {"name": "Detect Telnet", "protocol": "tcp", "dst_port": 23, "alert": "Telnet access attempt detected"},
    {"name": "Suspicious Payload", "payload_pattern": "malicious_content", "alert": "Suspicious payload found"}
  ]
}
```

---

## Notes

- You **must run as Administrator** to enable packet interception and sniffing.
- For production use, expand rules logic, add logging, refine IDS signatures, and consider real-time alerting.
- This project is educational and may need hardening for real-world deployment.

---

## Contributing

Pull requests welcome!  
Feel free to open issues for bugs, new feature suggestions, or questions.

---

## License

MIT License

