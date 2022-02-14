#!/usr/bin/env python3
from pprint import pprint
from sys import argv
import re
filename = argv[1]

#pattern =re.compile('''((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)''')
hosts =[]
with open(filename, 'r') as f:
    data = f.readlines()
    print(data)

for line in data:
    print(line)
    try:#hosts.append(
        ip = line.split('addr="')[1].split('" ')[0]
        port = int(line.split('portid="')[1].split('">')[0])
        with open('live_hosts.txt', 'a') as w:
             w.write(f'{ip}\n')
        w.close()
        if port in [80, 8080, 8443, 443]:
            with open('web_hosts.txt', 'a') as w:
                w.write(f'{ip}:{port}\n')
        else:
            with open(f'{port}.txt', 'a') as w:
               w.write(f'{ip}\n')
        w.close()
    except Exception as e:
        print(e)
        pass
