import sys


filename = sys.argv[1]
with open(filename, 'r') as f:
    data = f.readlines()

output = filename + ".out"
with open(output, 'a') as w:
    for d in data:
        if "hostname name" in d:
            hostname = d.split('="')[1].split('"')[0]
            print(hostname)
            w.write(hostname + '\n')
