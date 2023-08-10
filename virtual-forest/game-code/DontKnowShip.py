import socket

class DontKnowShip:
    def __init__(self):
        self.dns_over_https_providers = {
            "Cloudflare": "https://cloudflare-dns.com/dns-query",
            "Google": "https://dns.google/dns-query",
            "Quad9": "https://dns.quad9.net/dns-query",
        }
        self.local_dns_servers = ["127.0.0.1", "192.168.1.1"] # Example local DNS servers

    def explain_dns(self):
        print("DNS (Domain Name System) is a hierarchical and decentralized system that translates human-readable domain names into IP addresses.")
        print("It acts like a phonebook for the internet, allowing devices to communicate with each other.")
        print("DNS uses various record types, such as A, AAAA, MX, CNAME, etc., to define properties of domain names.")

    def local_dns_setup(self):
        print("Local DNS setup involves configuring a DNS server within a local network.")
        print("This can be used for caching, filtering, or custom domain resolution.")
        print("Common local DNS server software includes BIND, dnsmasq, Unbound, etc.")

    def dns_over_https(self, provider_name):
        provider_url = self.dns_over_https_providers.get(provider_name, None)
        if provider_url:
            print(f"DNS over HTTPS (DoH) encrypts DNS queries using HTTPS. {provider_name} provides DoH service at {provider_url}.")
        else:
            print(f"Provider {provider_name} not found in the known providers list.")

    def reverse_dns_lookup(self, ip_address):
        try:
            host_name = socket.gethostbyaddr(ip_address)
            print(f"The reverse DNS lookup for {ip_address} is {host_name}.")
        except socket.herror:
            print(f"Unable to perform reverse DNS lookup for {ip_address}.")

    def explore_dns_methods(self):
        print("Other DNS methods and configurations include:")
        print("- DNSSEC: Secures DNS responses using digital signatures.")
        print("- Split-horizon DNS: Provides different DNS information based on the client's location.")
        print("- Anycast DNS: Distributes DNS queries to multiple locations for load balancing.")
        print("- DNS over TLS (DoT): Encrypts DNS queries using TLS.")

if __name__ == "__main__":
    dont_know_ship = DontKnowShip()
    dont_know_ship.explain_dns()
    dont_know_ship.local_dns_setup()
    dont_know_ship.dns_over_https("Cloudflare")
    dont_know_ship.reverse_dns_lookup("8.8.8.8")
    dont_know_ship.explore_dns_methods()
