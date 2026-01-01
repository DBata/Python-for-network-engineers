#!/usr/bin/env python

base_addr= "192.168.254."
last_octet= 0
prefix_length= int(input("\nEnter a subnet prefix length between 25-30: "))

subnet_size_value= 32 - prefix_length
subnet_size= 2**subnet_size_value
no_of_subnets= 256 // subnet_size
exempt_hosts= 2
no_of_hosts= subnet_size - exempt_hosts
first_addr= f"{base_addr}1"
last_addr= f"{base_addr}{no_of_hosts}"
first_subnet= f"{base_addr}0"
second_subnet= f"{base_addr}{subnet_size}"

print()
print(f"Number of hosts per subnet: {no_of_hosts}")
print(f"Number of subnets: {no_of_subnets}")
print("\nSubnets:")
for subnet_no in range(no_of_subnets):
    subnet =f"{base_addr}{subnet_no * subnet_size}"
    print(f"Subnet: {subnet}")

print(f"\nFirst subnet:{first_subnet}")
print(f"First address: {first_addr}")
print(f"Last address: {last_addr}")


