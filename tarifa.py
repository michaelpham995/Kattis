

#! /user/bin/python3

import sys

def main():
    mb = int(input())
    months = int(input())
    print((mb * months) - sum([int(input()) for _ in range(months)]) + mb)
if __name__ == "__main__":
    main()
