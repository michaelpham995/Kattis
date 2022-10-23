

#! /user/bin/python3

import sys

def main():
    stopwatch = []
    for line in sys.stdin:
        stopwatch.append(int(line))
    if (len(stopwatch) - 1) % 2 == 1:
        print('still running')
    else:
        total = 0
        for x in range(1, len(stopwatch), 2):
            runningtime = stopwatch[x + 1] - stopwatch[x]
            total = runningtime + total
        print(total)

    
    
    
if __name__ == "__main__":
    main()
