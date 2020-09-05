def delete_dups(nums):
    valid_iterator = 0
    for i in range(len(nums)):
        if i != 0 and nums[i] != nums[i-1]:
            valid_iterator += 1
        nums[valid_iterator] = nums[i]
    for i in range(valid_iterator+1, len(nums)):
        nums[i] = 0
    return nums

print(delete_dups([2,3,5,5,7,11,11,11,13]))