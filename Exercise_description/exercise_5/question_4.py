#!/usr/bin/env python

import re
from rich import print


filename= "show_lldp.txt"
with open(filename) as f:
    lldp_data= f.read()

section_pattern= r"^Chassis id:.*?Vlan ID:[\w ]+"
results= re.findall(section_pattern, lldp_data, flags=re.DOTALL | re.M)

print()
for lldp_entry in results:
    #Initialze to null strings
    local_port, remote_system_name, remote_port = ("", "", "")
    m = re.search(r"^Port id: (\S+)", lldp_entry, flags=re.M)
    if m:
        remote_port = m.group(1)

    m = re.search(r"^Local Port id: (\S+)", lldp_entry, flags=re.M)
    if m:
        local_port= m.group(1)

    m = re.search(r"^System Name: (\S+)", lldp_entry, flags=re.M)
    if m:
        remote_system_name = m.group(1)

    print("-" *25)
    print(f"Local port: {local_port}")
    print(f"  Remote System: {remote_system_name}")
    print(f"  Remote Port: {remote_port}")
    print("-" *25)
    

print()

