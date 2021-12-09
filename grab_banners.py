#!/usr/bin/env python3

from sys import argv
from subprocess import check_output, STDOUT
import requests
requests.packages.urllib3.disable_warnings() 
import json
import colorama
from colorama import Fore
import re
from multiprocessing import Pool
import argparse

http_proxy  = "http://127.0.0.1:8080"
https_proxy = "https://127.0.0.1:8080"

title_pattern=re.compile(r'<title>(.*?)</title>', re.UNICODE )
parser = argparse.ArgumentParser(description='Utility for grabbing banners from a list of target IPs')
parser.add_argument('--threads', help='number of threads to use.', default=10)
parser.add_argument('--codes', help='Response status codes to show (e.g., 200, 404, 500) ', type=int, nargs='+', default=[200])
parser.add_argument('--targets', metavar='targets.txt', type=str,
                    required=True,
                    help='list of targets, one host per line')
parser.add_argument('--out', metavar='out.txt', required=False, type=str,
                    help='file to write valid hosts to')
parser.add_argument('--noproxy', help='Disable Burp proxying', type=bool, default=False)


proxyDict = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
            }

args = parser.parse_args()

print(args)
filename = args.targets
def output(body, headers, status, url):
    print(Fore.WHITE + f'Headers:')
    for k,v in headers.items():
            print(f'{k}: {v}')
    print(Fore.RESET + f'                    Status: [{status}]  ' + Fore.WHITE + f'{url}'  )
    if body != None:
        print(Fore.WHITE + f'-------------------------------------Page------------------------------------')
        print(Fore.WHITE + f'{body}')
        print(Fore.WHITE + f'----------------------------------------------------------------------------------')

def banner(host):
    try: 
            if '80' in host or '8080' in host:
                host = f'http://{host}'
            else:
                host = f'https://{host}'
            Fore.RESET
            url = f'{host}'.replace(' ','').replace('\n', '')
            if args.noproxy:
                req = requests.get(url, timeout=1, allow_redirects=True,verify=False)
            else:
                req = requests.get(url, timeout=1, allow_redirects=True,proxies=proxyDict,verify=False)
            body = req.text
            if len(body) > 100 and title_pattern.search(body).group(1) != None:
                body = title_pattern.search(body).group(1)
            status = (req.status_code)
            headers = req.headers
            if status == 200:
                status = Fore.GREEN + str(f'{status}'+Fore.RESET)
                headers = req.headers
                if args.out is not None:
                    with open(args.out,'a') as f:
                        f.write(host)
                f.close()
            if status == 404:
                status = Fore.YELLOW + str(f'{status}'+Fore.RESET)
            else:
                status = Fore.RED + str(f'{status}'+Fore.RESET)
            if req.status_code in args.codes:
                output(body, headers, status, url)
            
    except Exception as e:
        #print(e)
        pass
    
with open(filename, 'r') as f:
    hosts = f.readlines()
            
with Pool(5) as p:
        print(p.map(banner, hosts))
