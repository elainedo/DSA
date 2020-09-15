# Given an array arr of 4 digits, find the latest 24 hour time that can be 
# made using each digit exactly one

def largestTime(nums):
    max_time = -1

    def calculateTime(nums):
        nonlocal max_time
        h1, h2, m1, m2 = nums
        hour = h1*10 + h2 
        minute = m1*10 + m2
        if hour < 24 and minute < 60:
            time = hour*60 + minute
        else:
            time = -1
        max_time = max(time, max_time)
    
    def permutation(nums, start):
        if len(nums) == start:
            calculateTime(nums)
        for i in range(start, len(nums)):
            nums[i], nums[start] = nums[start], nums[i]
            permutation(nums, start+1)
            nums[i], nums[start] = nums[start], nums[i]

    permutation(nums, 0)

    if max_time == -1:
        return ""
    else:
        return "{:02d}:{:02d}".format(max_time // 60, max_time % 60)

print(largestTime([1,2,3,4]))