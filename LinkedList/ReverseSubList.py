from Node import *

def reverse_sub_list(head, m, n):
    dummy = ptr = Node(0)
    dummy.next = head
    for _ in range(1, m):
        ptr = ptr.next

    tail = ptr.next
    for _ in range(n-m):
        temp = ptr.next
        ptr.next = tail.next
        tail.next = tail.next.next
        ptr.next.next = temp

    return dummy.next

printLinkedList(reverse_sub_list(translateArrayToLinkedList([11, 3, 5, 7, 2]), 1, 3))