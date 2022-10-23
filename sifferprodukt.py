

#! /user/bin/python3
import sys

def main():
    n = input()
    while len(n) > 1:
        x = 1
        for c in n:
            if c != '0': x *= int(c)
        n = str(x)
    print(n)
    
if __name__ == "__main__":
    main()
