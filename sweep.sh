#!/bin/bash

#Beginner bash script that takes the first 3 octets of an IPV4 address and does a ping sweep of all hosts on that subnet.

echo "Enter the first 3 octets of an IPV4 address"

read ip

for x in {1..255}
do
	ping -c 1 $ip.$x | grep "64 bytes" | cut -d " " -f 4 | tr -d ":"
done

