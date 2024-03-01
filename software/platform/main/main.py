#!/usr/bin/env python3

from app import *

import os
import sys
from argparse import ArgumentParser

def main():

	p = ArgumentParser(
		prog=sys.argv[0],
		description="Badger main web platform.",
		epilog="For more info, contact badger@shawnd.xyz.",
	)
	p.add_argument(
		"ip",
		help="Server IP address to bind to.",
		nargs="?",
		type=str,
		default="127.0.0.1",
	)
	p.add_argument(
		"port",
		help="Server port to bind to.",
		nargs="?",
		type=int,
		default=8080,
	)
	p.add_argument(
		"-d", "--debug",
		help="Enable debugging mode.",
		action="store_true",
		default=False,
	)
	args = p.parse_args()

	settings = {
		"host"   : args.ip,
		"port"   : args.port,
		"debug"  : args.debug,
	}

	app.run(**settings)

if __name__ == "__main__":
	main()
