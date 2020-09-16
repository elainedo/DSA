class Node:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

def translateArrayToLinkedList(nums):
    dummy = ptr = Node(0)
    for num in nums:
        n = Node(num)
        ptr.next = n
        ptr = ptr.next
    return dummy.next

def translateLinkedListToArray(node):
    lst = []
    while node != None:
        lst.append(node.val)
        node = node.next
    return lst

