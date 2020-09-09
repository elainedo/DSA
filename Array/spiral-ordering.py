def spiralordering(nums):
    result = []
    for layer in range((len(nums)+1)//2):
        if layer == len(nums)//2:
            result.append(nums[layer][layer])

        # left to right
        for i in range(layer, len(nums)-layer-1):
            result.append(nums[layer][i])
        
        # top to bottom
        for i in range(layer, len(nums)-layer-1):
            result.append(nums[i][len(nums)-layer-1])

        # right to left
        for i in range(len(nums)-layer-1, layer, -1):
            result.append(nums[len(nums)-layer-1][i])

        # bottom to top
        for i in range(len(nums)-layer-1, layer, -1):
            result.append(nums[i][layer])

    return result

print(spiralordering([[1,2,3],[4,5,6],[7,8,9]]))
# 1, 2, 3, 6, 9, 8, 7, 4, 5

print(spiralordering([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
# 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10
