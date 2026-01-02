#!/usr/bin/env python

from rich import print

filename= "show_ip_int_brief.txt"
with open(filename) as f:
    data= f.read()

interface_ip= {}
for line in data.splitlines():
    interface, ip_addr, *_=line.split()

    if ip_addr in ["IP-Address","unassigned"]:
        continue

    interface_ip[interface]=ip_addr

print()
print(interface_ip)
print()


