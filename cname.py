import json
import sys

filename = sys.argv[1]


with open(f'{filename}'+'.txt', 'w') as w:
    with open(filename, 'r') as f:
        with open(f'{filename}'+'.hosts.txt', 'w') as w2:
            entries = f.readlines()
            for entry in entries:
                j = json.loads(entry)
                if j['port'] == '443':
                    hostname = " ".join(j['tls-grab']["dns_names"])
                    if len(hostname) > 5:
                        ip = str(j['input'])
                        w.write(f'{ip} {hostname}\n')
                        w2.write(f'{hostname}\n')
