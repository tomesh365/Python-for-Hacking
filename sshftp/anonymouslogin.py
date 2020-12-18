#!/usr/bin/python3

import ftplib


def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'anonymous')
        print("[+] " + hostname + " FTP anonymous login success. ")
        ftp.quit()
        return True
    except:
        print("[-] " + hostname + "FTP anonymous login failed ")


host = input("Enter the IP address: ")
anonLogin(host)
