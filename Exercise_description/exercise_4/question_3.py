#!/usr/bin/env python

from rich import print

vlans = [
    {
        "vlanshowbr-vlanid": "1",
        "vlanshowbr-vlanid-utf": "1",
        "vlanshowbr-vlanname": "default",
        "vlanshowbr-vlanstate": "active",
        "vlanshowbr-shutstate": "noshutdown",
    },
    {
        "vlanshowbr-vlanid": "2",
        "vlanshowbr-vlanid-utf": "2",
        "vlanshowbr-vlanname": "VLAN0002",
        "vlanshowbr-vlanstate": "active",
        "vlanshowbr-shutstate": "noshutdown",
    },
    {
        "vlanshowbr-vlanid": "3",
        "vlanshowbr-vlanid-utf": "3",
        "vlanshowbr-vlanname": "VLAN0003",
        "vlanshowbr-vlanstate": "active",
        "vlanshowbr-shutstate": "noshutdown",
    },
    {
        "vlanshowbr-vlanid": "4",
        "vlanshowbr-vlanid-utf": "4",
        "vlanshowbr-vlanname": "VLAN0004",
        "vlanshowbr-vlanstate": "active",
        "vlanshowbr-shutstate": "noshutdown",
    },
]

print(f"{'VLAN_ID':^10}{'VLAN_NAME':^20}")
print(f"{'-'*10:^10} {'-'*20:^20}")
for val in vlans:
    vlan_id= val["vlanshowbr-vlanid"]
    vlan_name= val["vlanshowbr-vlanname"]
    print(f"{vlan_id:^10} {vlan_name:^20}")

print()


