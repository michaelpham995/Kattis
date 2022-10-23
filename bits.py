import sys
nums = []
for line in sys.stdin.readlines():
    nums.append(int(line))
answers = []
numbers = [6,1,2,3,4,10,94]
for x in range(1, len(nums)):
    if nums[x] == 0:
        answers.append(nums[x])
    count = 0
    while nums[x] != 0:
        a = 0
        while pow(2, a) <= nums[x]:
            a += 1
        count += 1
        if pow(2, a) == nums[x]:
            nums[x] -= pow(2, a)
        nums[x] -= pow(2, a - 1)
    answers.append(count)
for x in range(len(answers)):
    print(answers[x])    
    
    


