def search_first_k(nums, k):
    left, right = 0, len(nums)-1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > k:
            right = mid - 1
        elif nums[mid] == k:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

print(search_first_k([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 108))