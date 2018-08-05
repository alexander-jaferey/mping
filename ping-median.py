#!/usr/bin/env Python3.6

import subprocess
import time
import sys
from statistics import median

nums = []

url = input("Address to ping> ")

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
