from argparse import ArgumentParser
from userlist import engine, export
import sys

def init_parser():
	parser = ArgumentParser()
	parser.add_argument('--path', help='the path to the export file')
	parser.add_argument('--format', help= 'Choose json or csv. Default is json.', default='json', choices=['json', 'csv'], type=str.lower)
	return parser

def main():
	args = init_parser().parse_args()
	users = engine.fetch_users()
	
	if args.path:
		file = open(args.path,'a',newline='')
	else:
		file = sys.stdout

	if args.format == 'json':
		export.to_json_file(users,file)
	else:
		export.to_csv_file(users,file)
	

	