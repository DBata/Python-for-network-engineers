Take the following Aruba CX "show vlan" output: arubacx_show_vlan.txt.

From this VLAN output create a dictionary where the key is the VLAN number and the corresponding value is the list of interfaces.

Note, constructing the list of interfaces will require that you separate and specify all of the individual interfaces. Additionally, some of the interfaces are currently specified using interface ranges, your program should properly this and should enumerate all of the individual interfaces.

Use rich.print to print the constructed dictionary to standard output.

Your output should look similar to the following:
{
    1: ['1/1/3', '1/1/4'],
    2: ['1/1/1', '1/1/3', '1/1/5'],
    3: ['1/1/2', '1/1/3', '1/1/5',
        '1/1/6', '1/1/7', '1/1/8',
        '1/1/9'],
    5: ['1/1/3'],
    10: ['1/1/3', '1/1/5'],
    11: ['1/1/3'],
    12: ['1/1/3', '1/1/6', 'lag1', 'lag2'],
    13: ['1/1/3', '1/1/6'],
    14: ['1/1/3', '1/1/6'],
    20: ['1/1/3', '1/1/10']
}


