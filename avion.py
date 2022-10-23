

#! /user/bin/python3

import sys

def main():
    stopwatch = []
    for line in sys.stdin:
        stopwatch.append(int(line))
    if len(stopwatch - 1) % 2 == 1:
        print('still running')
    else:
        x = stopwatch[-1] - stopwatch[-2]
        
        

    
    
    
if __name__ == "__main__":
    main()
