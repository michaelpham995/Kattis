

#! /user/bin/python3

import sys

def main():
    eye = input()
    bars = eye.split('()')
    print("correct" if len(bars[0])==len(bars[1]) else "fix")    
if __name__ == "__main__":
    main()
