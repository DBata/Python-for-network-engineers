#!/usr/bin/env python

base_addr= "192.18.254."
preffix_length =int(input("\nEnter a subnet preffix length(25-30): "))
subnet_size_value=32-preffix_length
subnet_size = 2**subnet_size_value
reserve_addr =2
no_of_hosts=subnet_size - reserve_addr
first_addr=f"{base_addr}1"
last_addr=f"{base_addr}no_of_hosts"
first_subnet = f"{base_addr}0"
second_subnet=f"{base_addr}{subnet_size}"
last_addr=f"{base_addr}{no_of_hosts}"


print(f"Number of hosts: {no_of_hosts}")
print("\nSubnets:")
print(f" First subnet: {first_subnet}")
print(f" Second subnet: {second_subnet}")
print(f"\nFirst subnet: {first_subnet}")
print(f" First Host Address: {first_addr}")
print(f" Last Host Address: {last_addr}")


