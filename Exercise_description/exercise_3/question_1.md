This exercise expands on the subnet calculations from lesson2, exercise1.

Create a base address variable and set it to "192.168.254.". Prompt a user to enter a subnet prefix length that ranges between 25 to 30 (i.e. the netmask length of the subnets). Save this input as an integer.

From the entered subnet prefix length, calculate the size of the subnet (the number of total IP addresses in the subnet). Once we know the subnet size, we can calculate the number of hosts allowed in the subnet (subtract off the network number and the broadcast address).

Use a loop to print out all of the subnet network numbers. For example, if your prefix length is 26, then your program should print out the following:
​Subnets:
 Number of subnets: 4
 Subnet Number: 192.168.254.0
 Subnet Number: 192.168.254.64
 Subnet Number: 192.168.254.128
 Subnet Number: 192.168.254.192

Your program should print out the following:
The number of hosts in the subnet.
The total number of subnets and the network number for each of the subnets
The first and last host address in just the first subnet.

