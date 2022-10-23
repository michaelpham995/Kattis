

#! /user/bin/python3

import sys

def main():
    teams = []
    for line in sys.stdin:
        line = line.split()
        names = [str(n) for n in line]
        teams.append(names)
    winners = []
    for x in range(1, len(teams)):
        if teams[x][0] not in winners and len(winners) < 24:
            winners.append(teams[x][0])
            winners.append(teams[x][1])
    for x in range(0, len(winners), 2):
        print(winners[x] + ' ' + winners[x + 1])
            
        

    
    
    
if __name__ == "__main__":
    main()
