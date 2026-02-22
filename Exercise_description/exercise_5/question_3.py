#!/usr/bin/env python

import re
from rich import print

filename= "arista_show_ip_arp.txt"
with open(filename) as f:
    arp_data= f.read()

ip_addr = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
mac_addr = r"\w+\.\w+\.\w+"
pattern = rf"^({ip_addr})\s+\S+\s+({mac_addr})\s+"
match_list = re.findall(pattern, arp_data, flags=re.M)

if match_list:
    arp_dict= dict(match_list)
    print(arp_dict)


