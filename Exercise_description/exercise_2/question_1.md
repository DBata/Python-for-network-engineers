Create a base address variable of "192.168.254.". Prompt a user to enter a subnet prefix length from between 25 to 30 (i.e. the netmask length of the subnets). Save this input as an integer.

From the entered subnet prefix length, calculate the size of the subnet (the number of total IP addresses in the subnet). Once we know the subnet size, we can calculate the number of hosts allowed in the subnet (subtract off the network number and broadcast address).

Also calculate and print out the network number for the first two subnets using the base address specified above.

Your program should print out the following:
a. The number of hosts in the subnet.
b. The network number of the first two subnets.
c. Both the first and last host address in the first subnet.

