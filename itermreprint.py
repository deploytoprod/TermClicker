#!/usr/bin/python

# itermreprint.py
# About: This application simulates users inputs on iTerm2 according to a line from an input file, addressed by the first file's line, and does not increments it for further uses.
# Author: Rafael Lopes <dev@rafalop.es>
# Author: Rafael Lopes <raf@amazon.com>
# Version: 1.0

from sys import stdout, argv
from time import sleep
from random import uniform

def main():
    path=str(argv[1])
    #print path

    f = open(path,'r')
    lines = f.readlines()
    f.close()

    head = int(lines[0])
    #print head
    #nexthead = head + 1

    line = lines[head-1]
    line = str(line)
    # if you see ^^^ remove everything after, including new line
    if "^^^" in line:
        line = line[:line.find("^^^")]

    for char in line:
        stdout.write(char)
        stdout.flush()
        sleep(uniform(0.01, 0.08))

    #sys.stdout.write(lines[head])

    #lines[0] = lines[0].replace(str(lines[0]), str(nexthead) + "\n")

    #with open(path, 'w') as fout:
    #  for line in lines:
    #    fout.write(line)

if __name__ == "__main__":
    main()
