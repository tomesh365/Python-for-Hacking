#!/usr/bin/python3

import crypt
from termcolor import colored


def crackPass(cryptWord):
    salt = cryptWord[0:2]
    dict = open('dictionary.txt','r')
    for word in dict.readlines():
        word = word.strip('\n')
        cryptPass = crypt.crypt(word, salt)
        if(cryptWord == cryptPass):
            print(colored("[+] Found password " + word, 'green'))
            return 

def main():
    passFile = open('userpass.txt', 'r')
    for line in passFile.readlines():
        if(":" in line):
            user = line.split(':')[0]
            cryptWord = line.split(':')[1].strip('').strip('\n')
            print("[+] Cracking password for " + user)
            crackPass(cryptWord)
            
if __name__ == "__main__":
    main()