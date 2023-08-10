class KnowThyShipMore:
    def __init__(self):
        self.local_ip_ranges = {
            "IPv4": [
                "10.0.0.0/8",
                "172.16.0.0/12",
                "192.168.0.0/16",
            ],
            "IPv6": [
                "fc00::/7",
            ],
        }
        self.dhcp_tips = [
            "DHCP (Dynamic Host Configuration Protocol) is used to assign IP addresses dynamically.",
            "A DHCP server can be set up to manage IP address allocation within a network.",
            "DHCP reservation allows specific IP addresses to be assigned to specific MAC addresses.",
            "DHCP options can be configured to provide additional network settings, such as DNS servers.",
        ]
        self.local_network_setup_tips = [
            "Choose a suitable local IP range based on network size and requirements.",
            "Set up a gateway device to manage traffic between the local network and external networks.",
            "Configure DHCP to manage IP address assignment and avoid conflicts.",
            "Implement proper network security measures, such as firewalls and access controls.",
            "Consider using Virtual LANs (VLANs) to segment the network for better management and security.",
        ]

    def explain_local_ips(self):
        print("Local IP Ranges:")
        for ip_version, ranges in self.local_ip_ranges.items():
            print(f"  {ip_version}: {', '.join(ranges)}")
        print("These ranges are reserved for private networks and are not routed on the public Internet.")

    def explain_dhcp(self):
        print("DHCP Tips:")
        for tip in self.dhcp_tips:
            print(f"  - {tip}")

    def explain_local_network_setup(self):
        print("Local Network Setup Tips:")
        for tip in self.local_network_setup_tips:
            print(f"  - {tip}")

if __name__ == "__main__":
    knowledge = KnowThyShipMore()
    knowledge.explain_local_ips()
    knowledge.explain_dhcp()
    knowledge.explain_local_network_setup()
