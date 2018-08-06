#!/usr/bin/env Python3.6

import subprocess
import argparse
from statistics import median

nums = []

parser = argparse.ArgumentParser(description="Get median ping time to an address")
parser.add_argument("address", help="Address to ping", nargs="?") 

args = parser.parse_args()

if args.address:
    ping = subprocess.run(["ping", "-c 6", args.address],
            encoding='utf-8',
            stdout=subprocess.PIPE
            )
else:
    url = input("Address to ping: ")
    ping = subprocess.run(["ping", "-c 6", url],
            encoding='utf-8',
            stdout=subprocess.PIPE
            )

ping = ping.stdout.splitlines()

for line in ping:
	if line.endswith("ms") and line.startswith("64"):
		line = line[-9:-3]
		num = float(line)
		nums.append(num) 

if nums != []:
    middle = median(nums)
    print(f"Median time is {middle} ms")
