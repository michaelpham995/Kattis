

#! /user/bin/python3
import sys

def main():
    data_to_list = []
    for line in sys.stdin:
        line = line.strip()
        data_to_list.append(line)
    count = 0
    for x in range(1, len(data_to_list) - 1):
        if data_to_list[x] == data_to_list[x + 1]:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
