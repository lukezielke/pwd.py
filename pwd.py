import argparse
import random
import os
import sys

symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
passwords = []
amount = 1
pw = ""
output_file = ""

parser = argparse.ArgumentParser(description='Create a secure Password with the specified length')

parser.add_argument('-l', '--length' , required=True, type=int, help='[REQUIRED] length of the password to create')
parser.add_argument('-a', '--amount' , required=False, type=int, help='[OPTIONAL] amount of passwords to create')
parser.add_argument('-o', '--output', required=False, type=str, help='[OPTIONAL] path to a .txt file to save the passwords in')

args = parser.parse_args()

length = args.length

#Check if a amount is specified and if so pass the amount into a int. Amount remains 1 if the argument is not specified
if args.amount is not None:
    amount = args.amount

#Generate the specified amounts of passwords and put them into a list.
for a in range(amount):
    pw = ""
    for l in range(length):
        pw = pw + random.choice(symbols)
    passwords.append(pw)

#Check if a output file is specified and check if it is a .txt file and if so put the passwords into the file. Else print the passwords to the console.
if args.output is not None:
    if args.output.lower().endswith(('.txt')):
        output_file = args.output
        with open(output_file, 'w') as f:
            for p in passwords:
                f.write(p+"\n")
    else: 
        print("[ERROR] The file specified is not a .txt file!")
else: 
    for p in passwords:
        print(p)


