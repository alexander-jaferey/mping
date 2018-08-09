#!/usr/bin/env Python3.6

import subprocess
import argparse
from math import ceil
from sys import stdout
from statistics import median

nums = []

parser = argparse.ArgumentParser(description="Get median ping time to an address")
parser.add_argument("--short", "-s", action="store_true", help="shortened output")
parser.add_argument("address", help="Address to ping", nargs="?")
args = parser.parse_args()

if args.address:
    ping = subprocess.run(["ping", "-c 6", args.address],
            encoding='utf-8',
            stdout=subprocess.PIPE
            )
else:
    url = input("Address to ping: ")
    ping = subprocess.run(["ping", "-c 5", url],
            encoding='utf-8',
            stdout=subprocess.PIPE
            )

ping = ping.stdout.splitlines()

for line in ping:
    if line.endswith("ms") and line.startswith("64"):
        line = line[-10:-3]
        num = float(line.strip("= "))
        nums.append(num) 

if nums != []:
    middle = "/" + str(median(nums))

if args.short:
    print(f"Median ping time is {middle.strip('/')}")
else:
    for line in ping:
        if not line.startswith("round"):
            print(line)
        else:
            words = line.split()
            words[1] += "/med"
            words[3] += middle
            stdout.write(" ".join(words))
