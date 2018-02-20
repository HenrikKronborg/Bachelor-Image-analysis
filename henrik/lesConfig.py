#!/usr/bin/env python3

f = open("config.txt", "r")
innstillinger = []

for linje in f:
    innstillinger.append(linje.strip("\n"))
print(innstillinger)
f.close()

