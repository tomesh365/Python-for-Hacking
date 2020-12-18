#!/usr/bin/python3

import hashlib

hashvalue = input("[+] Enter a string to Hash: ")

hashobj1 = hashlib.md5()
hashobj1.update(hashvalue.encode())
print("md5 Hash of " + hashvalue + ' is: ')
print(hashobj1.hexdigest())
print('\n')

hashobj2 = hashlib.sha1()
hashobj2.update(hashvalue.encode())
print("Sha1 Hash of " + hashvalue + ' is: ')
print(hashobj2.hexdigest())
print('\n')

hashobj3 = hashlib.sha224()
hashobj3.update(hashvalue.encode())
print("Sha224 Hash of " + hashvalue + ' is: ')
print(hashobj3.hexdigest())
print('\n')

hashobj4 = hashlib.sha256()
hashobj4.update(hashvalue.encode())
print("Sha256 Hash of " + hashvalue + ' is: ')
print(hashobj4.hexdigest())
print('\n')

hashobj5 = hashlib.sha512()
hashobj5.update(hashvalue.encode())
print("Sha512 Hash of " + hashvalue + ' is: ')
print(hashobj5.hexdigest())
print('\n')