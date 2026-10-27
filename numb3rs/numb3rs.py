# CS50P Week7
# Objectif : This program validates IPv4 addresses
# according to standard format rules.
# Usage: Run the program and enter an IPv4 address when prompted
# Validation Rules:
#   - Format: X.X.X.X where X is 0-255
#   - No leading zeros (except for 0 itself)
#   - Four octets separated by periods
# Examples of valid addresses:
#   192.168.1.1
#   10.0.0.255
#   0.0.0.0
import re


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    pattern = r"""^(25[0-5]|2[0-4]\d|1[0-9]\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1[0-9]\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1[0-9]\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1[0-9]\d|[1-9]?\d)$"""
    matches = re.search(pattern, ip, re.VERBOSE)
    if matches:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
