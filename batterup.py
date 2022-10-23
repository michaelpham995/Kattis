

#! /user/bin/python3

import sys
        
    

def main():

    hits = []
    for line in sys.stdin:
        line = line.split()
        hits.append(line)
    divider = 0
    total = 0
    for x in range(0, len(hits[1])):
        if int(hits[1][x]) >= 0:
            divider += 1
            total += int(hits[1][x])
    slugging = total / divider
    print(slugging)
            
             

        

    
    
    
if __name__ == "__main__":
    main()
