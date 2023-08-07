import random

class Networking:
    def __init__(self):
        self.connected_devices = ["Device1", "Device2", "Device3"]
        self.connections = {}  # This could be a dictionary representing the network connections

    def introduce(self):
        return f"Welcome to the Virtual Network! The devices currently connected are {', '.join(self.connected_devices)}."

    def add_device(self, new_device):
        self.connected_devices.append(new_device)
        return f"{new_device} has been added to the network."

    def remove_device(self, device_to_remove):
        if device_to_remove in self.connected_devices:
            self.connected_devices.remove(device_to_remove)
            return f"{device_to_remove} has been removed from the network."
        else:
            return f"{device_to_remove} is not in the network."

    def connect_devices(self, device1, device2):
        # In a real implementation, this method would create a connection between the two devices.
        # For simplicity, we'll just add them to the connections dictionary.
        self.connections[device1] = device2
        self.connections[device2] = device1
        return f"{device1} and {device2} are now connected."

    def send_data(self, sender, receiver, data):
        # In a real implementation, this method would handle data transmission between devices.
        # For simplicity, we'll just generate a random response indicating successful transmission.
        response = random.choice(["Data received and processed.", "Transmission successful.", "Data sent successfully."])
        return f"Sending data from {sender} to {receiver}: {data}. Response: {response}."

    def disconnect_devices(self, device1, device2):
        # In a real implementation, this method would disconnect the two devices.
        # For simplicity, we'll just remove them from the connections dictionary.
        if device1 in self.connections:
            del self.connections[device1]
        if device2 in self.connections:
            del self.connections[device2]
        return f"{device1} and {device2} are now disconnected."

    def get_network_status(self):
        # In a real implementation, this method would provide detailed network status information.
        # For simplicity, we'll just return a basic message indicating the number of connected devices.
        num_devices = len(self.connected_devices)
        return f"There are currently {num_devices} devices connected to the network."

# Create an instance of Networking and interact with it
network = Networking()

# Get the initial network status
print(network.introduce())

# Add a new device to the network
print(network.add_device("Device4"))

# Connect two devices
print(network.connect_devices("Device1", "Device2"))

# Send data between connected devices
print(network.send_data("Device1", "Device2", "Hello, this is a test message!"))

# Disconnect the devices
print(network.disconnect_devices("Device1", "Device2"))

# Get the updated network status
print(network.get_network_status())
