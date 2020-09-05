def next_permutation(nums):
    # find the non increasing part at the end 
    last_index = len(nums)-2
    while (last_index >= 0):
        if nums[last_index] < nums[last_index+1]:
            break
        last_index -= 1
    if last_index == -1:
        nums[:] = reversed(nums)
        return nums

    for i in reversed(range(last_index+1, len(nums))):
        if nums[i] > nums[last_index]:
            nums[i], nums[last_index] = nums[last_index], nums[i]
            break

    nums[last_index+1:] = reversed(nums[last_index+1:])
    return nums



print(next_permutation([6,2,1,5,4,3,0]))