# Configuration file for the Network Traffic Analyzer

# Network interface to capture packets from
INTERFACE = 'en0'  # Ensure this is the correct interface for your network

# Number of packets to capture
PACKET_COUNT = 10  # Adjust based on your needs

# Filter criteria for packet capture
FILTER_CRITERIA = {
    'ip_dst': None,  # Set to None to capture all destination IPs
    'protocol': None  # Set to None to capture all protocols
}

# Logging configuration
LOGGING = {
    'enabled': True,  # Enable or disable logging
    'file': 'network_traffic.log',  # Ensure this path is valid and writable
    'level': 'INFO'  # Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
}

# Packet display settings
DISPLAY_SETTINGS = {
    'show_ip_src': True,  # Display source IP
    'show_ip_dst': True,  # Display destination IP
    'show_protocol': True  # Display protocol
}

# Packet capture timeout (in seconds)
CAPTURE_TIMEOUT = 60  # Adjust based on how long you want to capture packets

# Example for capturing only specific ports (if applicable)
PORT_FILTER = {
    'tcp_ports': [80, 443],  # List of TCP ports to filter
    'udp_ports': [53]  # List of UDP ports to filter
}

# Alert settings
ALERT_SETTINGS = {
    'enabled': False,  # Enable or disable alerts
    'threshold': 100,  # Packet count threshold for triggering an alert
    'alert_message': 'High packet traffic detected!'  # Alert message
}
