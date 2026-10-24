from classes import Node, LinkedList

def merge_sorted_lists(list1, list2):
    dummy = Node()
    tail = dummy

    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        if current1.data < current2.data:
            tail.next = current1
            current1 = current1.next
        else:
            tail.next = current2
            current2 = current2.next
        tail = tail.next

    if current1:
        tail.next = current1
    elif current2:
        tail.next = current2

    merged_list =LinkedList()
    merged_list.head = dummy.next
    return merged_list