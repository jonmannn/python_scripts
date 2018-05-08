#!/usr/bin/python3
"""
convert_xml.py Takes convert to Windows style newlines from provided mac/unix file
"""

import sys

if len(sys.argv) < 2:
    print('Error: No file specified. Please supply the full path to the file you are trying to convert')
    exit()

filename = sys.argv[1]

fileContents = open(filename, "r").read()
f = open(filename, "w", newline="\r\n")
f.write(fileContents)
f.close()

print('Conversion complete!')