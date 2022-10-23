

#! /user/bin/python3

import sys

def main():
    advertise = []
    for line in sys.stdin:
        line = line.split()
        numbers = [int(n) for n in line]
        advertise.append(numbers)
    for x in range(1, len(advertise)):
        if advertise[x][1] > (advertise[x][0] + advertise[x][2]):
            print('advertise')
        elif advertise [x][1] == (advertise[x][0] + advertise[x][2]):
            print('does not matter')
        else:
            print('do not advertise')
        
    
    
if __name__ == "__main__":
    main()
