Expand on exercise1, once again you will be using the show_ip_int_brief.txt file. For this exercise, include all interfaces (i.e. both interfaces with and without an IP address). For each interface construct a dictionary where the key is the interface name and the corresponding value is another dictionary. The inner dictionary should contain the following three keys (and the associated values): "ip_addr", "line_status", "line_protocol".

For example, GigabitEthernet0/0/0 should look as follows:
​'GigabitEthernet0/0/0': {
        'ip_addr': '10.220.88.22',
        'line_status': 'up',
        'line_protocol': 'up'
    }
Enclose all of the individual interface dictionaries in a larger dictionary.

The larger dictionary will contain all of the interfaces as the keys and the corresponding inner interface dictionaries as the values (with the inner dictionaries containing the "ip_addr", "line_status", and "line_protocol" key-value pairs).

Print this larger dictionary to standard output using rich.print.
