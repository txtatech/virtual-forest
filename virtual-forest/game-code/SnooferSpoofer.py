class SnooferSpoofer:
    def __init__(self):
        self.spoofing_techniques = {
            "MAC Address Spoofing": {
                "description": "Changing the Media Access Control (MAC) address to disguise the hardware.",
                "tools": ["macchanger", "ifconfig"],
                "example": "sudo macchanger --random eth0"
            },
            "IP Address Spoofing": {
                "description": "Hiding the true IP address by using a fake one.",
                "tools": ["iptables", "arpspoof"],
                "example": "sudo arpspoof -i eth0 -t target_IP gateway_IP"
            },
            "Email Spoofing": {
                "description": "Forging the sender's address in an email header.",
                "tools": ["sendemail"],
                "example": 'sendemail -f "spoofed@example.com" -t "target@example.com" -u "Subject" -m "Message"'
            },
            "DNS Spoofing": {
                "description": "Redirecting DNS queries to a malicious server.",
                "tools": ["dnsspoof"],
                "example": "sudo dnsspoof -i eth0 -f hosts.txt"
            },
            "ARP Spoofing": {
                "description": "Associating a MAC address with the IP address of another host.",
                "tools": ["arpspoof"],
                "example": "sudo arpspoof -i eth0 -t target_IP gateway_IP"
            },
            "Web Spoofing": {
                "description": "Creating a fake website to gather personal information.",
                "tools": ["setoolkit"],
                "example": "sudo setoolkit"
            }
        }

    def teach_spoofing(self):
        print("Welcome to the world of spoofing! Here are some common spoofing techniques:")
        for technique, details in self.spoofing_techniques.items():
            description = details["description"]
            tools = ', '.join(details["tools"])
            example = details["example"]
            print(f"- {technique}: {description}\n  Tools: {tools}\n  Example: {example}")

if __name__ == "__main__":
    snoofer_spoofer = SnooferSpoofer()
    snoofer_spoofer.teach_spoofing()
