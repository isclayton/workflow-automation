# bb_utils
Some things to automate pentesting workflow


## make_target_list.py
Takes one argument, a file with hosts. Will regex search for IPs in the file and make a clean list called targets.txt

## parse_hosts_from_masscan.py 
Separates out hosts based on port into a few seperate lists. 

## grab_banners.py

See `-h`. grabs banners from web hosts over http(s). 
