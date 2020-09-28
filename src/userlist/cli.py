from argparse import ArgumentParser

def init_parser():
	parser = ArgumentParser()
	parser.add_argument('--path', help='the path to the export file')
	parser.add_argument('--format', default='json', choices=['json', 'csv'], type=str.lower)
	return parser

