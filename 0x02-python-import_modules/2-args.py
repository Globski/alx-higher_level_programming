#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    count = len(argv) - 1
    print("{} {}{}".format(count, "argument" if count == 1 else "arguments", ":" if count > 0 else "."))

    for i in range(1, count + 1):
        print("{}: {}".format(i, argv[i]))
