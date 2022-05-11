import argparse
import json
import sys

def parse(filename):
	with open(filename, 'r') as r:
		data = json.loads(r.read())
	domain = data['endpoint'].split('/')[3]
	subs = []
	for sub in data['subdomains']:
		subs.append(f"{sub}.{domain}")
	return subs

def parseStdin(input):
	#print(input)
	data = json.loads(input)
	domain = data['endpoint'].split('/')[3]
	subs = []
	for sub in data['subdomains']:
		subs.append(f"{sub}.{domain}")
	return subs

def main():

	parser = argparse.ArgumentParser(description='create target list from sectrails api output')
	parser.add_argument('file', metavar='N', type=str, help='json file containing subdomains (or @- to accept stdin)')

	args = parser.parse_args()
	data = []
	if args.file == "@-":
		inputs = sys.stdin.read()
		for line in inputs:
			data = parseStdin(inputs)
	else:
		data = parse(args.file)
	#print(data)
	for subdomain in data:
		print(subdomain)





if __name__ == "__main__":
    main()

