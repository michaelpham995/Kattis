

#! /user/bin/python3

import sys
        
    

def main():
    n = int(input())
    for x in range(n):
        string = input().split(",")
        total = 0
        for x in range(len(string)):
            temp = string[(-x) - 1]
            if temp.isdigit():
                total += int(temp) * pow(60, x)
        print(total)
            
    

            
             

        

    
    
    
if __name__ == "__main__":
    main()
