def days(num):
    printer = 1
    days = 0
    while printer < num:
        printer *= 2
        days += 1
    days += 1
    return days

print(days(int(input())))

