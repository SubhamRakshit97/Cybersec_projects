def filter_packet(packet, ip_dst=None, protocol=None):
    if packet.haslayer('IP'):
        ip_src = packet['IP'].src
        ip_dst_packet = packet['IP'].dst
        protocol_packet = packet['IP'].proto
        
        if (ip_dst and ip_dst != ip_dst_packet) or (protocol and protocol != protocol_packet):
            return False
        return True
    return False
