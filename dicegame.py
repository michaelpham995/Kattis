

#! /user/bin/python3

import sys

def middle(low, high):
    return low + (high - low) / 2

def main():
    ga1, gb1, ga2, gb2 = list(map(int, input().split()))
    ea1, eb1, ea2, eb2 = list(map(int, input().split()))

    gunnar_value = middle(ga1, gb1) + middle(ga2, gb2)
    emma_value = middle(ea1, eb1) + middle(ea2, eb2)

    if gunnar_value > emma_value:
        print("Gunnar")
    elif emma_value > gunnar_value:
        print("Emma")
    else:
        print("Tie")
    
    
if __name__ == "__main__":
    main()
