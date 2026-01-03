You have the following data-structure from a Cisco NX-OS device (note, this is a list of dictionaries):
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
Loop over this list and print out all of the VLAN IDs and their corresponding VLAN names.

Note, you will need to embed the above data structure into your Python program.









