QUESTION ONE(1)
You can start a simple telnet connection using the following code:
from telnetlib import Telnet
import time

host = "device.domain.com"
username = "admin"

# Create telnet connection
tn = Telnet(host)

# Wait for the device to respond
time.sleep(1.5)
data = tn.read_very_eager()
print(data)

If connecting to a Cisco router your output will likely be similar to the following:
b'\r\n\r\nUser Access Verification\r\n\r\nUsername: '

Note, this is a byte-string and we can convert it to a unicode string by calling the .decode() method on the byte-string.

Using the above, create a read() function that takes two arguments: telnet_conn and sleep. Default the sleep argument to 1.5 seconds. In this function perform the sleep, telnet channel read, byte-string decoding, and return the read data.

Your new telnet code should now look as follows (intentionally not showing the read() function that you are supposed to create).
host = "device.domain.com"
username = "admin"

# Create telnet connection
tn = Telnet(host)
data = read(tn)
print(data)



QUESTION TWO(2)
At this point, we are telnetting but have not fully logged in. In order to fully login, we need to be able to handle the username/password prompting. For my Cisco IOS device this looks like the following:
$ telnet cisco1.lasthop.io
Trying 184.105.247.70...
Connected to cisco1.lasthop.io.
Escape character is '^]'.

User Access Verification

Username: pyclass
Password: 

cisco1#

In order to handle the Username prompt we need to write data to the channel. This can be accomplished by using the telnetlib .write() method. The .write() method takes a byte-string.

So we need to search for "Username" in the data that we read and then send "admin\n" (don't forget the <enter> at the end). We need to send this username as a byte-string.

In order to send it as a byte-string, we simply call the .encode() method on our unicode string. This will convert our internal string to a UTF-8 encoded byte-string (think of UTF-8 encoding as representing our internal string in a certain standardized way to the remote device).

Create a new 'write' function that takes in both the telnet connection and also some data (i.e. the data that you will send to the remote device). The function should convert this data to UTF-8 (i.e. a UTF-8 encoded byte string) and send it down the telnet channel.

Now that you have both a read() function and a write() function. Use these two functions to read in the initial data, perform a regular expression search on that data looking for the Username (or whatever your test device presents here) and then writes out the username ("admin\n" in my example).

Perform one final read() and verify that you receive the "Password" prompt back (or whatever the equivalent is on your test device).



QUESTION THREE(3)
Expand on exercise2 except use your read() and write() functions to properly handle both the username prompting and the password prompting. Use Python's getpass() to have the script prompt for the password.

Perform one final read() and verify that you are fully logged in to the device.



QUESTION FOUR(4)
Modify the code that you created in exercise2 and exercise3 and create a login() function.

This login() function should handle both sending the username and sending the password. Your code should use regular expressions to detect both the username and the password prompt.

After sending the password, your code should verify that you have fully logged in successfully. In other words, you should have a regular expression search that matches the network device's prompt. Your login() function should return a boolean indicating that it detected the network device's prompt (True) or that it failed to do so (False).

Your login() function should accept three arguments: the telnet_connection, the username, and the password. In your test code, pass these three arguments in as named arguments.



QUESTION FIVE(5)
Create a show_cmd() function that sends a command down the telnet channel and reads back the command output.

The function should take two arguments: telnet_conn and cmd. The cmd parameter should have a default value of "show ip interface brief" (or some similar command that works on your test device).

Have your function return the output from this command.

Back in your main program, call your show_cmd() function using both the default 'cmd' and then again with a separate 'cmd' of your choice. Pass the telnet_connection in as a positional argument and the cmd in as a named argument (this assumes that telnet_conn is the first parameter in the function definition).



