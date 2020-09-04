def can_reach_end(nums):
    i, farthest = 0, 0
    while i <= farthest and farthest < len(nums):
        farthest = max(farthest, i + nums[i])
        i += 1
    return farthest >= len(nums)-1

print(can_reach_end([3,3,7,0,2,0,1]))
print(can_reach_end([3,2,0,0,2,0,7]))