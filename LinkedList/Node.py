class Node:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

def translateArrayToLinkedList(nums):
    dummy = ptr = Node(0)
    for num in nums:
        n = Node(num)
        ptr.next = n
        ptr = ptr.next
    return dummy.next

def printLinkedList(node):
    while node != None:
        print(node.data, end = " ")
        node = node.next
