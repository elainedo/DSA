def dutch_national_flag(nums):
    lo, mid, hi = 0, 0, len(nums)-1
    while mid <= hi:
        if nums[mid] == 0:
            nums[lo], nums[mid] = nums[mid], nums[lo]
            lo += 1
        elif nums[mid] == 2:
            nums[hi], nums[mid] = nums[mid], nums[hi]
            hi-=1
        mid += 1
    return nums

print(dutch_national_flag([1,0,2,1,1,0,2,1]))