#!/usr/bin/env python3

from sys import argv
import re
filename = argv[1]

pattern =re.compile('''((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)''')
 

with open(filename, 'r') as f:
    data = f.read().replace('\n', '').split('/32')
    print(data)



with open('targets.txt', 'w') as w:
    for host in data:
        if len(host) != 0:
            w.write(host+"\n")