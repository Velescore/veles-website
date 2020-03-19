#!/usr/bin/env python3
"""
Runs tasks related to the web application life-cycle

Copyright (C) 2020 The Veles Core developers

This program is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation, either version 3
of the License, or (at your option) any later version.
"""
import os
import argparse

from app.builder import WebPageBuilder
from app.wiki.builder import WikiBuilder
from app.news.builder import NewsBuilder

# Basic commandline interface
def main():
	package_dir = os.path.dirname(os.path.realpath(__file__))
	parser = argparse.ArgumentParser(description='Veles Core website management tool')

	parser.add_argument('--path', default=package_dir,
		help='path to the veles-website package base directory')
	parser.add_argument('action', 
		help='supported actions: build-index, build-wiki, build-news')
	args = parser.parse_args()

	# Sanity check for the path argument
	if not os.path.exists(args.path):
		raise ValueError('invalid --path: path does not exist: {}'.format(args.path))

	elif not os.path.isdir(args.path):
		raise ValueError('invalid --path: not a directory: {}'.format(args.path))

	elif not os.path.isdir(os.path.join(args.path, 'templates')):
		raise ValueError('invalid --path: not a veles-website base directory: {}'.format(args.path))

	# Actions
	if args.action == 'build-index':
		builder = WebPageBuilder(args.path)
		builder.build_index()

	elif args.action == 'build-wiki':
		builder = WikiBuilder(args.path)
		builder.build_articles()

	elif args.action == 'build-news':
		builder = NewsBuilder(args.path)
		builder.build_articles()

	else:
		raise ValueError('unsupported action: {}'.format(args.action))

if __name__=='__main__':
	#try:
	main()
	#except ValueError as e:
	#    print(os.path.basename(__file__) + ': error: {}'.format(str(e)))
