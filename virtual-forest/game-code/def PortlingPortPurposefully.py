def PortlingPortPurposefully():
    """
    PortlingPortPurposefully function provides information about various ports and their purposes,
    as well as how to use netstat to check for open ports on a system.

    Returns:
        str: Information about ports and their purposes, along with netstat usage instructions.
    """
    port_info = {
        20: "FTP (File Transfer Protocol) - Used for transferring files over a network.",
        80: "HTTP (Hypertext Transfer Protocol) - Used for serving web pages.",
        443: "HTTPS (Hypertext Transfer Protocol Secure) - Used for secure web browsing.",
        22: "SSH (Secure Shell) - Used for secure remote login and command execution.",
        25: "SMTP (Simple Mail Transfer Protocol) - Used for sending email messages.",
        110: "POP3 (Post Office Protocol version 3) - Used for receiving email messages.",
        143: "IMAP (Internet Message Access Protocol) - Used for accessing and managing email messages.",
        53: "DNS (Domain Name System) - Used for resolving domain names to IP addresses.",
        123: "NTP (Network Time Protocol) - Used for synchronizing the system time of network devices.",
        3306: "MySQL - Used for accessing MySQL databases.",
        3389: "RDP (Remote Desktop Protocol) - Used for remote desktop connections.",
        8080: "HTTP Proxy - Used for forwarding HTTP requests and responses.",
        8888: "Jupyter Notebook - Used for interactive computing and data analysis.",
    }

    info_str = "Ports and Their Purposes:\n\n"
    for port, purpose in port_info.items():
        info_str += f"Port {port}: {purpose}\n"

    info_str += "\nHow to Use netstat to Check for Open Ports:\n"
    info_str += "You can use the netstat command to display a list of open ports on your system.\n"
    info_str += "Open a terminal or command prompt and enter the following command:\n"
    info_str += "netstat -an | findstr LISTEN\n"
    info_str += "This will show a list of all open ports that are currently listening for incoming connections.\n"

    return info_str

# Example usage:
ports_and_purposes = PortlingPortPurposefully()
print(ports_and_purposes)
