

#! /user/bin/python3

import sys

def main():
    inputs = []
    for line in sys.stdin:
        inputs.append(float(line))
    x = int(round(inputs[0] * 1000 * 5280 / 4854))
    print(x)


    
    
    
if __name__ == "__main__":
    main()
