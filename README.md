# pwd.py
This is a python cli tool that i wrote mainly to learn how to write a cli tool in python but is also kind of useful.
The main goal is to create secure passwords in your command line.

# Features
- obviously create secure passwords
- create passwords in bulk
- output passwords to terminal or to a specified .txt file

# Usage
Create a password with specified length:
```
python pwd.py -l <length>
```
Create multiple passwords:
```
python pwd.py -l <length> -a <amount>
```
Save passwords in a specified .txt file:
```
python pwd.py -l <length> -a <amount> -o <path to file>
