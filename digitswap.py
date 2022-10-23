

#! /user/bin/python3

import sys

def main():
    line = sys.stdin.readline()
    line2 = sys.stdin.readline()
    
    print(line * (line2 + 1) - sum(line + line2) for a in range(line2))
    
    
if __name__ == "__main__":
    main()
