

#! /user/bin/python3
import sys

def main():
    for line in sys.stdin:
        value1, value2, value3, value4 = list(map(float, line.split()))
        print(abs((value3 - value1) * (value4 - value2)))

if __name__ == "__main__":
    main()
