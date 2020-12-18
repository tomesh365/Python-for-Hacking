#!/usr/bin/python3

from termcolor import colored
import hashlib


def tryOpen(wordlist):
    global pass_file
    try:
        pass_file = open(wordlist, 'r')
    except expression as identifier:
        print("[-] No such file at that path!")
        quit()


pass_hash = input("[+] Enter md5 hash value: ")
wordlist = input("[+] Enter pasth to the password file: ")
tryOpen(wordlist)

for word in pass_file:
    print(colored("[-] Trying " + word.strip("\n"), 'red'))
    enc_wrd = word.encode('utf-8')
    md5ddigest = hashlib.md5(enc_wrd.strip()).hexdigest()

    if md5ddigest == pass_hash:
        print(colored("[+] Password found " + word, 'green'))
        exit()

print(colored("[-] password not in the list", 'red'))
