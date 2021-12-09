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
        if port in [80, 8080, 8443, 443]:
            with open('web_hosts.txt', 'a') as w:
                w.write(f'{ip}:{port}\n')
        elif port in [3306, 5432, 1521, 1830, 1433, 1434,27017, 27018, 27019, 28017,6379,5984,7000, 7001, 9042]:
            with open('db_hosts.txt', 'a') as w:
                w.write(f'{ip} # {port} \n')
        elif port in [5556, 7001, 7002, 8001, 8005, 8009, 3389]:
            print("PWN HOST FOUND")
            with open('pwn_hosts.txt', 'a') as w:
                w.write(f'{ip} # {port} \n')
        else:
            with open('odd_hosts.txt', 'a') as w:
               w.write(f'{ip} # {port} \n')
        w.close()
    except Exception as e:
        print(e)
        pass
#pprint(hosts)
#with open('targets.txt', 'w') as w:
#    for host in data:
#        if len(host) != 0:
#            w.write(host+"\n")



