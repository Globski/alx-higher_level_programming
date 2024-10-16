#!/usr/bin/python3
"""
101-stats.py

This script reads from standard input and computes metrics from log entries.
It processes lines in the format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

After every 10 lines and upon a keyboard interruption (CTRL + C), it prints:
- Total file size: The sum of all previous file sizes
- Number of lines by status code:
    Possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500
"""

import sys


def parse_log():
    """Parses log entries from stdin and computes metrics.

    Args:
        total_size (int): The total size of all processed files.
        status_codes (dict): A dictionary containing counts
        of each status code.
    """
    total_size = 0
    status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }

    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            if len(parts) < 9:
                continue

            try:
                status_code = parts[-2]
                file_size = int(parts[-1])
            except (IndexError, ValueError):
                continue

            total_size += file_size

            if status_code in status_codes:
                status_codes[status_code] += 1

            if line_count % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        sys.exit()

    print_metrics(total_size, status_codes)

def print_metrics(total_size, status_codes):
    """Prints the current metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


if __name__ == "__main__":
    parse_log()
