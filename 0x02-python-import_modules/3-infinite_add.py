#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

if len(argv) > 1:
    print(sum(int(arg) for arg in argv[1:]))
else:
    print("0")
