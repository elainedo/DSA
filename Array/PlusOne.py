def plus_one(nums):
    for i in reversed(range(len(nums))):
        print(i)
        result = nums[i]+1
        if (result < 10):
            nums[i] += 1
            return nums
        nums[i] = 0
    if nums[0] == 0:
        nums.append(0)
        nums[0] = 1
    return nums

print(plus_one([9,9,9,9]))
print(plus_one([1,2,3]))
print(plus_one([0]))
