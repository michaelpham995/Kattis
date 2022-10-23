

#! /user/bin/python3

import sys

def main():
    for line in sys.stdin:
        if line != '':
            a, b = line.split()
            a = int(a)
            b = int(b)
            maximum = max(a, b)
            minimum = min(a, b)
            print(minimum, maximum)
    
    
if __name__ == "__main__":
    main()
