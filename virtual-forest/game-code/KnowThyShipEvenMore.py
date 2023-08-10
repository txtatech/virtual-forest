class KnowThyShipEvenMore:
    def __init__(self):
        self.topics = {
            "Subnetting and Supernetting": {
                "Description": "Learn how to divide or combine IP address ranges for efficient network management.",
                "Subnet Masks": "Understand how subnet masks define the size of subnets.",
                "CIDR Notation": "Explore CIDR notation for specifying IP address ranges.",
                "Subnet Design Strategies": "Gain insights into designing subnets based on network requirements.",
            },
            "Network Address Translation (NAT)": {
                "Description": "Discover techniques to map private IP addresses to public IPs for Internet communication.",
                "Static NAT": "Learn about one-to-one mapping of IP addresses.",
                "Dynamic NAT": "Understand how to dynamically assign public IPs from a pool.",
                "Port Forwarding": "Explore port-based redirection for specific services.",
            },
            "Quality of Service (QoS)": {
                "Description": "Optimize network performance by prioritizing traffic based on requirements.",
                "Traffic Classification": "Learn to categorize traffic types for QoS treatment.",
                "Bandwidth Allocation": "Understand how to allocate bandwidth to different traffic classes.",
                "QoS Policies": "Explore setting up QoS policies for effective traffic management.",
            },
            "IPv6 Transition Mechanisms": {
                "Description": "Get insights into transitioning from IPv4 to IPv6 networks.",
                "Dual-Stack": "Learn about running IPv4 and IPv6 concurrently.",
                "Tunneling": "Explore techniques like 6to4 and ISATAP for tunneling IPv6 over IPv4.",
                "NAT64/DNS64": "Understand mechanisms to facilitate communication between IPv4 and IPv6 networks.",
            },
            "Network Monitoring and Security": {
                "Description": "Master network monitoring tools and security practices.",
                "Packet Analysis": "Learn to analyze network packets using Wireshark or tcpdump.",
                "Firewalls": "Explore firewall types (stateful, stateless) and rule configurations.",
                "Intrusion Detection/Prevention": "Understand how to detect and prevent network intrusions.",
                "Secure VPNs": "Explore secure Virtual Private Network (VPN) setups.",
            },
            "Software-Defined Networking (SDN)": {
                "Description": "Discover the paradigm of separating network control from data forwarding.",
                "Controllers": "Learn about SDN controllers like OpenDaylight or Floodlight.",
                "Switches": "Understand OpenFlow-enabled switches for dynamic network control.",
                "Network Automation": "Explore automating network management tasks.",
            },
        }

    def explore_topics(self):
        print("Welcome to the KnowThyShipEvenMore class!")
        print("This class provides advanced insights into networking concepts and configurations.")

        while True:
            print("\nAvailable Topics:")
            for index, topic in enumerate(self.topics, start=1):
                print(f"{index}. {topic}")

            choice = input("Choose a topic to explore (or 'exit' to leave): ")
            if choice.lower() == 'exit':
                break

            try:
                topic_index = int(choice) - 1
                selected_topic = list(self.topics.keys())[topic_index]
                self.show_topic_info(selected_topic)
            except (ValueError, IndexError):
                print("Invalid choice. Please select a valid topic number or 'exit'.")

    def show_topic_info(self, topic):
        if topic in self.topics:
            print(f"\nTopic: {topic}")
            description = self.topics[topic]["Description"]
            print(f"Description: {description}")
            print("\nSubtopics:")
            for subtopic, sub_description in self.topics[topic].items():
                if subtopic != "Description":
                    print(f"- {subtopic}: {sub_description}")
        else:
            print("Topic not found. Please select a valid topic.")

if __name__ == "__main__":
    know_thy_ship_even_more = KnowThyShipEvenMore()
    know_thy_ship_even_more.explore_topics()
