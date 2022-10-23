

#! /user/bin/python3

import sys

def main():
    words = []
    for line in sys.stdin:
        if line != '':
            words.append(line)
    for x in range(1, len(words), 2):
        print(words[x])
        

    
    
if __name__ == "__main__":
    main()
