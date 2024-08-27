from scapy.all import sniff, conf
import pandas as pd
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='network_traffic.log', level=logging.INFO)

def initialize_csv(filename):
    with open(filename, 'w') as f:
        f.write('Source,Destination,Protocol\n')

def packet_callback(packet):
    if packet.haslayer('IP'):
        ip_src = packet['IP'].src
        ip_dst = packet['IP'].dst
        protocol = packet['IP'].proto
        data = {
            'Source': ip_src,
            'Destination': ip_dst,
            'Protocol': protocol,
        }
        # Log and save packet details
        logging.info(data)
        df = pd.DataFrame([data])
        df.to_csv(filename, mode='a', header=False, index=False)
        print(data)  # Optional: Print packet details to console

def start_sniffing(interface):
    print(f"Starting packet capture on {interface}...")
    sniff(iface=interface, prn=packet_callback, count=10)  # Adjust count or use timeout

def get_timestamped_filename():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f'network_traffic_{timestamp}.csv'

if __name__ == "__main__":
    filename = get_timestamped_filename()
    initialize_csv(filename)
    print("Available network interfaces:")
    print(conf.ifaces)
    INTERFACE = 'en0'  # Update with your network interface
    start_sniffing(INTERFACE)
