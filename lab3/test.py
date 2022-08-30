#!/usr/bin/env python3
import sys

name = sys.argv[1]
name += "abcdef"

print(
    """.i 3
.o 8
.ilb x y z
.ob a b c d e f g h"""
)
for i in range(6):
    char = name[i]
    if i == 0:
        char = char.upper()
    print(f"{bin(i)[2:].zfill(3)} {bin(ord(char))[2:].zfill(8)}")
print(".e")
