#!/usr/bin/python

# itermprint.py
# About: This application simulates users inputs on iTerm2 according to a line from an input file, addressed by the first file's line, and increments it for further uses.
# Author: Rafael Lopes <dev@rafalop.es>
# Version: 1.0

from sys import stdout, argv
from time import sleep
from random import uniform

path=str(argv[1])
#print path

f = open(path,'r')
lines = f.readlines()
f.close()

head = int(lines[0])
#print head
nexthead = head + 1

line = lines[head]
line = str(line)

for char in line:
    if char == '\n':
      sleep(uniform(0.05,1.08))
    stdout.write(char)
    stdout.flush()
    sleep(uniform(0.01, 0.08))


#sys.stdout.write(lines[head])

lines[0] = lines[0].replace(str(lines[0]), str(nexthead) + "\n")

with open(path, 'w') as fout:
  for line in lines:
    fout.write(line)
