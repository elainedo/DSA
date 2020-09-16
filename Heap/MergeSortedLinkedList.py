from heapq import heappush, heappop
from Node import *

def mergeSortedLinkedList(sortedLists):
    min_heap = []

    for i in range(len(sortedLists)):
        if sortedLists[i]:
            heappush(min_heap, (sortedLists[i].val, i, sortedLists[i]))

    dummy = ptr = Node()
    while min_heap:
        val, index, node = heappop(min_heap)
        ptr.next = Node(val)
        ptr = ptr.next

        if node.next:
            heappush(min_heap, (node.next.val, index, node.next))

    return dummy.next

[[1,4,5,6],[3,5,7],[],[0,6,8,9]]
lst1 = translateArrayToLinkedList([1,4,5,6])
lst2 = translateArrayToLinkedList([3,5,7])
lst3 = translateArrayToLinkedList([])
lst4 = translateArrayToLinkedList([0,6,8,9])

sortedLists = [lst1, lst2, lst3, lst4]

print(translateLinkedListToArray(mergeSortedLinkedList(sortedLists)))