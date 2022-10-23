

#! /user/bin/python3

import sys

def main():
    line = sys.stdin.readline()
    line2 = sys.stdin.readline()
    if len(line) >= len(line2):
        print("go")
    else:
        print('no')
    
    
if __name__ == "__main__":
    main()
