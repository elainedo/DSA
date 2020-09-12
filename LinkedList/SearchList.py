from Node import *

def search_list(lst, key):
    while lst and lst.data != key:
        lst = lst.next
    return lst

lst = Node(2)
lst.next = Node(3)
