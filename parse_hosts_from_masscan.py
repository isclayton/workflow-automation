#!/usr/bin/env python3
from pprint import pprint
from sys import argv
import re
import argparse 

parser = argparse.ArgumentParser(description='Parse output of masscan')

parser.add_argument('--file', help='masscan XML output', required=True, default="")

parser.add_argument('-p', help='port(s) to parse out', required=False, default="")
parser.add_argument('-o', help='output file', required=True, default="out.txt")

args = parser.parse_args()

hosts =[]
with open(args.file, 'r') as f:
    data = f.readlines()
    print(data)

for line in data:
    print(line)
    try:
        ip = line.split('addr="')[1].split('" ')[0]
        port = int(line.split('portid="')[1].split('">')[0])
        hosts.append(ip)
        if args.p and port in args.p:
            with open(f'{args.o}', 'a') as w:
                w.write(f'{ip}:{port}\n')
        elif not args.p and port in []:
            with open('web_hosts.txt', 'a') as w:
                w.write(f'{ip}:{port}\n')
        else:
            with open(f'{port}.txt', 'a') as w:
               w.write(f'{ip}\n')
        w.close()
    except Exception as e:
        print(e)
        pass

hosts = list(set(hosts))
for host in hosts:
    with open('live_hosts.txt', 'a') as w:
        w.write(f'{host}\n')
    w.close()