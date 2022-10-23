

#! /user/bin/python3

import sys

def main():
    putin = []
    for line in sys.stdin:
        line = line.split()
        code = [int(n) for n in line]
        putin.append(code)
    if putin[0][0] != 0 and putin[0][1] != 0 and putin[0][2] != 0:
        if putin[0][0] + putin[0][1] + putin[0][2] >= putin[0][3] and putin[0][3] >= 3:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')

            


        

    
    
    
if __name__ == "__main__":
    main()
