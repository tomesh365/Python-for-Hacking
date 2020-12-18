#!/usr/bin/python3

from urllib.request import urlopen
import hashlib
from termcolor import colored


sha1hash = input("[+] Enter Sha1 Hash Value: ")

passlist = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')

for password in passlist.split('\n'):
    hashguess = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()
    if (hashguess == sha1hash):
        print(colored("[+] the password is " + str(password), 'green'))
        quit()
    else:
        print(colored("[-] password guess " + str(password) +
                      'does not match, trying next...', 'red'))

print("[*] password not in password list")
