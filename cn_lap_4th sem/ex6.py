import socket
import struct
import binascii

def create_arp_request(sender_mac, sender_ip, target_ip):
    # Ethernet frame
    eth_header = struct.pack("!6s6s2s", 
                             binascii.unhexlify("ffffffffffff"),  # Destination MAC: Broadcast
                             binascii.unhexlify(sender_mac),       # Source MAC
                             b'\x08\x06')                          # EtherType: ARP

    # ARP packet
    arp_packet = struct.pack("!HHBBH6s4s6s4s", 
                             1,                                    # Hardware type: Ethernet
                             0x0800,                               # Protocol type: IPv4
                             6,                                    # Hardware size
                             4,                                    # Protocol size
                             1,                                    # Opcode: request
                             binascii.unhexlify(sender_mac),       # Sender MAC
                             socket.inet_aton(sender_ip),          # Sender IP
                             binascii.unhexlify("000000000000"),   # Target MAC
                             socket.inet_aton(target_ip))          # Target IP

    return eth_header + arp_packet

def send_arp_request(interface, sender_mac, sender_ip, target_ip):
    raw_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
    raw_socket.bind((interface, socket.SOCK_RAW))
    arp_request = create_arp_request(sender_mac, sender_ip, target_ip)
    raw_socket.send(arp_request)

if __name__ == "__main__":
    interface = "eth0"  # Change to your network interface
    sender_mac = "001122334455"  # Sender MAC address
    sender_ip = "192.168.1.100"  # Sender IP address
    target_ip = "192.168.1.1"  # Target IP address
    send_arp_request(interface, sender_mac, sender_ip, target_ip)


import socket
import struct
import binascii

def create_arp_reply(sender_mac, sender_ip, target_mac, target_ip):
    # Ethernet frame
    eth_header = struct.pack("!6s6s2s", 
                             binascii.unhexlify(target_mac),       # Destination MAC: Target's MAC
                             binascii.unhexlify(sender_mac),       # Source MAC
                             b'\x08\x06')                          # EtherType: ARP

    # ARP packet
    arp_packet = struct.pack("!HHBBH6s4s6s4s", 
                             1,                                    # Hardware type: Ethernet
                             0x0800,                               # Protocol type: IPv4
                             6,                                    # Hardware size
                             4,                                    # Protocol size
                             2,                                    # Opcode: reply
                             binascii.unhexlify(sender_mac),       # Sender MAC
                             socket.inet_aton(sender_ip),          # Sender IP
                             binascii.unhexlify(target_mac),       # Target MAC
                             socket.inet_aton(target_ip))          # Target IP

    return eth_header + arp_packet

def send_arp_reply(interface, sender_mac, sender_ip, target_mac, target_ip):
    raw_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
    raw_socket.bind((interface, socket.SOCK_RAW))
    arp_reply = create_arp_reply(sender_mac, sender_ip, target_mac, target_ip)
    raw_socket.send(arp_reply)

if __name__ == "__main__":
    interface = "eth0"  # Change to your network interface
    sender_mac = "001122334455"  # Sender MAC address
    sender_ip = "192.168.1.1"  # Sender IP address
    target_mac = "66778899aabb"  # Target MAC address
    target_ip = "192.168.1.100"  # Target IP address
    send_arp_reply(interface, sender_mac, sender_ip, target_mac, target_ip)
