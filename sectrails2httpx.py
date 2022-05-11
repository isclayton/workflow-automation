import argparse
import json

def parse(filename):
	with open(filename, 'r') as r:
		data = json.loads(r.read())
	domain = data['endpoint'].split('/')[3]
	subs = []
	for sub in data['subdomains']:
		subs.append(f"{sub}.{domain}")
	return subs
def main():

	parser = argparse.ArgumentParser(description='create target list from sectrails api output')
	parser.add_argument('file', metavar='N', type=str, help='json file containing subdomains')
	parser.add_argument('--api', help='api key')

	args = parser.parse_args()
	data = parse(args.file)
	for subdomain in data:
		print(subdomain)





if __name__ == "__main__":
    main()

