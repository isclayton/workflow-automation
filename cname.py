import json
import sys

filename = sys.argv[1]


with open(f'hostfile.txt', 'w') as w:
    with open(filename, 'r') as f:
        with open(f'hostnames.txt', 'w') as w2:
            entries = f.readlines()
            for entry in entries:
                j = json.loads(entry)
                if j['port'] == '443':
                    cname = str(j['tls-grab']["common_name"][0])
                    hosts_entry = " ".join(j['tls-grab']["dns_names"])
                    hostnames = " \n".join(j['tls-grab']["dns_names"])
                    print(cname)
                    print(hostnames)
                    if len(hostnames) > 5:
                        ip = str(j['input'])
                        w.write(f'{ip} {cname} {hosts_entry}\n')
                        w2.write(f"{cname}\n {hostnames}")
