#!/bin/python3

#Beginner python script that takes the first 3 octets of an IPV4 address and does a ping sweep of all hosts on that subnet.

import subprocess
import argparse

def ip_sweeper(ip_address):
	for i in range(1,255):
		address = args.IP+"."+str(i)
		subprocess.call(["ping", address, "-c 1"])

parser = argparse.ArgumentParser()
parser.add_argument("IP", help="First 3 octets of an IPV4 address")
args = parser.parse_args()

three_octets = args.IP

ip_sweeper(three_octets)
