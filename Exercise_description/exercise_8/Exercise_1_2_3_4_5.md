QUESTION ONE(1)
Create a data class named RouterFacts.

This class should have the following attributes: hostname, vendor, network_os, model, os_version, interfaces, uptime_sec, and serial_number. All the attributes should be strings (type str), except for interfaces (which should be a list, type List) and uptime_sec (which should be an integer, type int).

Create an instance of this class using the following data.
{
    'hostname': 'la-rtr1',
    'vendor': 'cisco',
    'network_os': 'iosxr',
    'model': '8201-SYS',
    'os_version': '7.0.12',
    'interfaces': [
        'HundredGigE0/0/0/24',
        'HundredGigE0/0/0/25',
        'HundredGigE0/0/0/26',
        'HundredGigE0/0/0/27',
        'HundredGigE0/0/0/28',
        'HundredGigE0/0/0/29',
        'HundredGigE0/0/0/30',
        'HundredGigE0/0/0/31',
        'HundredGigE0/0/0/32',
        'HundredGigE0/0/0/33',
        'HundredGigE0/0/0/34',
        'HundredGigE0/0/0/35',
        'MgmtEth0/RP0/CPU0/0'
    ],
    'uptime_sec': 93073,
    'serial_number': 'FOC2291AVYB'
}
Print out this object to standard output.

Note, for type List, you will need to import the following:
from typing import List




QUESTION TWO(2)
Create a Router class that has two class attributes: count and all_hosts.

"count" should be initialized to 0 and all_hosts should be initialized to a blank list.

The class should have one instance attribute named host (instance attribute i.e. bound to self in dunder-init()).

As part of dunder-init(), each Router object that you create should set the aforementioned "host" attribute and should increment the class "count" attribute. Additionally, each Router object that you create should add the "host" name to the "all_hosts" list.

In other words, "count" should count the total number of Router objects that exist and "all_hosts" is a list of all the hostnames (of Router objects). Note, we are not taking any action for deleted objects (in other words, you do not need to handle Router object deletion).

Create four Router objects.

Print out the two class attributes: count, and all_hosts.

Verify that the count is 4 and that all_hosts has all four of the "host" names.




QUESTION THREE(3)
Create a class hierarchy where the parent class is NetworkDevice and takes a "host" attribute in dunder-init().

Create three child classes named Router, Switch, and AccessPoint. Each of these three classes should inherit from NetworkDevice and should use the dunder-init() method.

The three child classes should have one additional method dunder-repr (i.e. __repr__ ). This method is a representation of an object. It generally shows you what it would look like to recreate the object.

Consequently, an example dunder-repr output for a Router object would be:
Router('rtr1.domain.com')
Create one object of each child class (Router, Switch, and AccessPoint).

For each of these objects, print out the "host" attribute and also print out the object itself. Note, if you have not defined dunder-str, Python will fallback and use dunder-repr. Consequently, printing out the object here will print out the dunder-repr that you created.




QUESTION FOUR(4)
Expand on exercise3, such that the Router class can accept an additional argument named "model" in dunder-init().

This "model" parameter should default to None. The dunder-init() method should assign the "model" to the object. Additionally, you should use super() to call the dunder-init() method of the parent class (so that the "host" attribute gets set properly).

Additionally create a print_model() method in the Router class that prints out the model assigned to the object (if the model is not None).

Create a Router class object that specifies both a host and a model. Print out the host attribute, the model attribute, and the object itself (you do not need to update dunder-repr to account for the model attribute). Finally, execute the print_model() method on this Router object.




QUESTION FIVE(5)
Create two classes: a Router class and a Channel class.

The Channel class should have four methods: dunder-init(), connect(), read(), and write().

Create two child classes of the Channel class: SSHChannel and TelnetChannel.

Both the SSHChannel class and the TelnetChannel class should have a dunder-init() method that calls super() on the parent class and that sets the transport attribute. Additionally, these two classes should also have a connect() method.

The connect() method of each of these child classes should just print a pretend message (i.e. we are pretending we are actually connecting). For example, "Fictional SSH connection to host1.domain.com".

The parent Channel class should accept three arguments in dunder-init(): host, username, and password. It should bind all of these arguments to the object.

The read() and write() method in the parent class should just print a message. Once again we are doing a fictional read and write. The write() method should accept a second argument named "data" (i.e. the data we would write out to the channel).

For the other main class, the Router class, you should accept five arguments: host, device_type, username, password, and transport. The transport parameter should default to "ssh". In dunder-init(), you should assign both the "host" and the "device_type" arguments to the object.

You should also check the transport: if the transport is "ssh", then you should create an instance of the SSHChannel class and assign this to self.channel of the Router object. In other words, the Router object will refer to this other object using "self.channel". You could call the connect() method on this SSHChannel object.

Similarly if the transport is "telnet", then you should create an instance of the TelnetChannel class and assign this object to self.channel of the Router object. Once again you should call the connect() method on this TelnetChannel object.

Finally, the Router class should have both a read() and write() method. The "read" method should call self.channel.read() and the "write" method should call self.channel.write(data). The "write" method should require a second argument named "data" (i.e. the data to write out the channel).

Create an instance of your Router class using a transport of "ssh". Do a test write() call and read() call on this Router object. Verify that you see the fictional messages that you expect.




