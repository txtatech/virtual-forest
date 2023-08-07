import subprocess

def ping_host(hostname):
    """
    ping_host function demonstrates the usage of 'ping' to check the reachability of a host.

    Args:
        hostname (str): The name or IP address of the host to ping.

    Returns:
        str: The output of 'ping' command containing the ping results.
    """
    try:
        # Run the 'ping' command using subprocess
        result = subprocess.run(['ping', '-c', '4', hostname], capture_output=True, text=True)
        if result.returncode == 0:
            # 'ping' command was successful
            return result.stdout
        else:
            # 'ping' command returned a non-zero exit code (indicating an error)
            return f"ping command failed with error: {result.stderr}"
    except Exception as e:
        return f"An error occurred while running ping: {str(e)}"

def whois_host(hostname):
    """
    whois_host function demonstrates the usage of 'whois' to retrieve domain information.

    Args:
        hostname (str): The domain name to look up.

    Returns:
        str: The output of 'whois' command containing domain information.
    """
    try:
        # Run the 'whois' command using subprocess
        result = subprocess.run(['whois', hostname], capture_output=True, text=True)
        if result.returncode == 0:
            # 'whois' command was successful
            return result.stdout
        else:
            # 'whois' command returned a non-zero exit code (indicating an error)
            return f"whois command failed with error: {result.stderr}"
    except Exception as e:
        return f"An error occurred while running whois: {str(e)}"

def finger_user(username):
    """
    finger_user function demonstrates the usage of 'finger' to get information about a user.

    Args:
        username (str): The username of the user to query.

    Returns:
        str: The output of 'finger' command containing user information.
    """
    try:
        # Run the 'finger' command using subprocess
        result = subprocess.run(['finger', username], capture_output=True, text=True)
        if result.returncode == 0:
            # 'finger' command was successful
            return result.stdout
        else:
            # 'finger' command returned a non-zero exit code (indicating an error)
            return f"finger command failed with error: {result.stderr}"
    except Exception as e:
        return f"An error occurred while running finger: {str(e)}"

def sonar_echo(hostname):
    """
    sonar_echo function demonstrates the usage of various network commands to echo information about a host.

    Args:
        hostname (str): The name or IP address of the host to echo.

    Returns:
        str: The combined output of 'ping', 'whois', and 'finger' commands for the host.
    """
    echo_result = ""

    # Execute and combine the results of ping, whois, and finger commands
    echo_result += f"=== Ping Results ===\n"
    echo_result += ping_host(hostname) + "\n"

    echo_result += f"=== Whois Results ===\n"
    echo_result += whois_host(hostname) + "\n"

    echo_result += f"=== Finger Results ===\n"
    echo_result += finger_user(hostname) + "\n"

    return echo_result

# Example usage:
host_to_echo = "example.com"
print(sonar_echo(host_to_echo))
