from Node import *

def merge_list(lst1, lst2):
    dummy = ptr = Node(0)
    while lst1 and lst2:
        if lst1.data < lst2.data:
            ptr.next = lst1
            lst1 = lst1.next
        else:
            ptr.next = lst2
            lst2 = lst2.next
        ptr = ptr.next
    ptr.next = lst1 or lst2
    return dummy.next


lst1 = translateArrayToLinkedList([1, 3, 5, 7, 9, 10, 11])
lst2 = translateArrayToLinkedList([2, 4, 6, 8])

merged = merge_list(lst1, lst2)
