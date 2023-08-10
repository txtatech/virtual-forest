import ipaddress

class KnowThyShip:
    def __init__(self):
        self.ipv4_examples = ["192.168.1.1", "10.0.0.1"]
        self.ipv6_examples = ["2001:db8::ff00:42:8329", "fe80::200:f8ff:fe21:67cf"]

    def explain_ipv4(self):
        print("IPv4 (Internet Protocol version 4) uses 32-bit addresses.")
        print("It's typically expressed in quad-dotted decimal format, e.g., 192.168.1.1.")
        print("There are five classes of IPv4 addresses: A, B, C, D, and E.")
        print("Special IPv4 addresses include loopback (127.0.0.1), private ranges (e.g., 192.168.x.x), and broadcast addresses.")

    def explain_ipv6(self):
        print("IPv6 (Internet Protocol version 6) uses 128-bit addresses.")
        print("It's expressed in hexadecimal notation separated by colons, e.g., 2001:db8::ff00:42:8329.")
        print("IPv6 has a more extensive address space and improved routing and network autoconfiguration.")

    def explain_subnetting(self):
        print("Subnetting divides an IP network into smaller, more manageable pieces.")
        print("It's used to optimize network performance and simplify management.")

    def explain_routing(self):
        print("Routing is the process of forwarding IP packets from one network to another.")
        print("Static routing is manually configured, while dynamic routing uses protocols like OSPF and BGP.")

    def explain_nat(self):
        print("Network Address Translation (NAT) allows private IP addresses to be translated into a public IP address.")
        print("NAT is common in home routers to allow multiple devices to share a single public IP.")

    def validate_ip(self, ip):
        try:
            ip_obj = ipaddress.ip_address(ip)
            print(f"{ip} is a valid {'IPv4' if ip_obj.version == 4 else 'IPv6'} address.")
        except ValueError:
            print(f"{ip} is not a valid IP address.")

if __name__ == "__main__":
    know_thy_ship = KnowThyShip()
    know_thy_ship.explain_ipv4()
    know_thy_ship.explain_ipv6()
    know_thy_ship.explain_subnetting()
    know_thy_ship.explain_routing()
    know_thy_ship.explain_nat()
    know_thy_ship.validate_ip("192.168.1.1")
    know_thy_ship.validate_ip("2001:db8::ff00:42:8329")
