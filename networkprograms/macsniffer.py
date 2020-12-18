#!/usr/bin/python

import socket
from struct import *


def eth_addr(pkt):
    b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(pkt[0]), ord(
        pkt[1]), ord(pkt[2]), ord(pkt[3]), ord(pkt[4]), ord(pkt[5]))
    return b 


try:
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
except:
    print("[-] Error on creating Socket object")
    exit(0)

while(True):
    packet = s.recvfrom(65535)
    packet = packet[0]

    eth_length = 14
    eth_header = packet[:eth_length]

    eth = unpack('!6s6sH', eth_header)  # first 14 protocol
    eth_protocol = socket.ntohs(eth[2])
    print("[+] Destination mac: " + eth_addr(packet[0:6]) +
          " [+] Source Mac: " + eth_addr(packet[6:12]) + "[+] protocol: " + str(eth_protocol))
