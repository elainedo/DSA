from heapq import heappush, heappop

def mergeSortedArray(sorted_arrays):
    min_heap = []

    for i in range(len(sorted_arrays)):
        if len(sorted_arrays[i]) == 0:
            continue
        heappush(min_heap, (sorted_arrays[i][0], i, 0))

    result = []
    while min_heap:
        element, array_num, index = heappop(min_heap) 
        result.append(element)

        if index+1 < len(sorted_arrays[array_num]):
            heappush(min_heap, (sorted_arrays[array_num][index+1], array_num, index+1))
    return result

print(mergeSortedArray([[1,4,5,6],[3,5,7],[],[0,6,8,9]]))