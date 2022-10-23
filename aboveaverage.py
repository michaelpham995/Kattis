

#! /user/bin/python3
import sys

def main():
    x = int(input())
    for y in range(x):
        numbers = input()
        num = numbers.split()
        total = 0
        for z in range(1, len(num)):
            total += int(num[z])
        average = total / int(num[0])
        counter = 0
        for z in range(1, len(num)):
            if (int(num[z]) > average):
                counter += 1
        print('%.3f' % (counter/int(num[0])*100) + '%')

if __name__ == "__main__":
    main()
