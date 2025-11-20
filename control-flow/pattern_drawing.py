#!/usr/bin/env python3

size = int(input("Enter the size of the pattern: "))

row = 0
while row < size:
    for col in range(size):
        print("*", end="")
    print()        # Move to the next line after finishing a row
    row += 1       # Go to the next row