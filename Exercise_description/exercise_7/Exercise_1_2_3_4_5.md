QUESTION ONE(1)
Create a NetworkDevice class that accepts four arguments: host, platform, username, and password. Assign these arguments to the object inside of dunder-init() method. In other words, inside of dunder-init(), you should have code that does the following (for all four of the attributes):
  self.host = host
Create a dunder-str() method that returns a string representation of the object and includes both the host attribute and the platform attribute in said string.

From this class, create two NetworkDevice objects and print the objects out to standard output.

Your output should look similar to the following:
  NetworkDevice: host1.domain.com (cisco_xe)
  NetworkDevice: host2.domain.com (juniper_junos)




QUESTION TWO(2)
Create an Interface class that accepts the following five arguments: intf_name, intf_mode, access_vlan, speed, and duplex. Assign these arguments to the object inside of dunder-init() method. Your dunder-init() method should have default values for the following parameters intf_mode="access", access_vlan=1, speed="1Gbps", duplex="full" (so only "intf_name" does not have a default value).

The definition of your dunder-init() method should look similar to the following:
    def __init__(
        self,
        intf_name,
        intf_mode="access",
        access_vlan=None,
        speed="1Gbps",
        duplex="full",
    ):
Inside of your dunder-init() method you should assign all of the attributes to the corresponding argument values.

Additionally, your dunder-init() method should contain certain checks. For "intf_mode", your dunder-init() method should check that the value is either "access" or "trunk". If the value is neither of these, then you should raise a ValueError exception.

If the "intf_mode" is access, then you should also check that the "access_vlan" is an integer. If the intf_mode is trunk, then you should set the "access_vlan" attribute to None.

Additionally, create a dunder-str() method that will display details about the interface when the object is printed.

Initialize seven Interface objects with the details specified below (the output of your program should also be similar to this):
Interface: Et1 (1Gbps/full, Mode: access, Vlan: 1)
Interface: Et2 (1Gbps/full, Mode: access, Vlan: 2)
Interface: Et3 (1Gbps/full, Mode: access, Vlan: 3)
Interface: Et4 (1Gbps/full, Mode: access, Vlan: 4)
Interface: Et5 (1Gbps/full, Mode: access, Vlan: 5)
Interface: Et6 (1Gbps/full, Mode: access, Vlan: 6)
Interface: Et7 (1Gbps/full, Mode: trunk)




QUESTION THREE(3)
A). Create an "OSPFRouter" class that represents one router running OSPF. This OSPFRouter class should accept the following arguments in dunder-init(): instance_id, area_id, router_id, is_dr, and is_bdr. All of these arguments should be bound as attributes to the object. Both the "is_dr" and the "is_bdr" parameters should default to False (in the dunder-init() parameter definition).

Additionally, create a private attribute named _neighbors in dunder-init(). This attribute should be initialized to an empty set.

B). Add a dunder-str() method that prints out a representation of a OSPFRouter object. This string representation should include all of the above attributes (including _neighbors).

C). Create an instance of this OSPFRouter class representing the following OSPF state:
arista2#show ip ospf database

            OSPF Router with ID(10.220.88.29) (Instance ID 42) (VRF default)

                 Router Link States (Area 0.0.0.0)

Link ID       ADV Router    Age  Seq#        Checksum Link count
10.220.88.28  10.220.88.28  582  0x80000008  0xa410   1
10.220.88.30  10.220.88.30  307  0x80000006  0xa40c   1
10.220.88.32  10.220.88.32  297  0x80000008  0x9c0c   1
10.220.88.34  10.220.88.34  292  0x80000006  0x9c08   1
10.220.88.31  10.220.88.31  305  0x80000005  0xa40a   1
10.220.88.33  10.220.88.33  292  0x80000006  0x9e09   1
10.220.88.29  10.220.88.29  581  0x80000007  0xa40e   1
10.220.88.35  10.220.88.35  287  0x80000006  0x9a07   1

Note, Arista2 is the designated router for this area (Area 0).




QUESTION FOUR(4)
Update your NetworkDevice class from exercise1 by converting the password attribute to a private attribute (named _password).

Add an @property for the 'password' attribute such that you retrieve the private password attribute and convert all of its characters over to "*" characters. Consequently, whenever anyone accesses nd_obj.password all they will see is "*" characters (obviously this is not real security as nd_obj._password would still show the cleartext password).

Create a setter property for the password attribute. The setter should verify that you are not setting the password to the exact same value as the previous password. If the passwords are identical a ValueError exception should be raised. If the password is new, then your code should update the private password attribute.




QUESTION FIVE(5)
Recreate your Interface class from Exercise2 except this time use an @property and a setter for both intf_mode and for access_vlan.

For both of these attributes you should use a private attribute i.e. self._intf_mode and self._access_vlan.

For the @property getter (for both attributes) just have the getter return the private attribute.

For the intf_mode setter, you should check that the new value is either "access" or "trunk". If any other value is used, raise an exception. If intf_mode is set to trunk, then you set the access_vlan attribute to None.

For the access_vlan setter, you should verify that the VLAN ID is an integer (if intf_mode is "access"). If the VLAN ID is not an integer, then you should raise a ValueError exception. If intf_mode is trunk, then you should always set the access_vlan value to None. In other words, any "intf_obj.access_vlan = value" operation should result in "intf_obj.access_vlan = None" (if the interface is trunking).



