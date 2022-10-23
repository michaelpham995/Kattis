

#! /user/bin/python3

from sys import stdin

def main():
    for line in stdin:
        if line == '':
            break
        value1, value2 = list(map(int, line.split()))
        print(abs(value1 - value2))
    
    
if __name__ == "__main__":
    main()
