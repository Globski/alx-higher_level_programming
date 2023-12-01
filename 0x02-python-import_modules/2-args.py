#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    count = len(argv) - 1
    plural = "s" if count != 1 else ""
    punctuation = ":" if count > 0 else "."

    print("{} {}{}".format(count, "argument" + plural, punctuation))

    for i in range(1, count + 1):
        print("{}: {}".format(i, argv[i]))
