from classes import Node, LinkedList

def merge_sort(linked_list):
    if linked_list.head is None or linked_list.head.next is None:
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    if linked_list is None or linked_list.head is None:
        left_half = linked_list
        right_half = None
        return left_half, right_half
    
    slow = linked_list.head
    fast = linked_list.head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        
    left_half = LinkedList()
    left_half.head = linked_list.head
    right_half = LinkedList()
    right_half.head = slow.next
    slow.next = None

    return left_half, right_half

def merge(left, right):
    merged = LinkedList()
    merged.head = merge_nodes(left.head, right.head)
    return merged

def merge_nodes(left, right):
    if left is None:
        return right    
    if right is None:
        return left
    
    if left.data < right.data:
        result = left
        result.next = merge_nodes(left.next, right)
    else:
        result = right
        result.next = merge_nodes(left, right.next)
    return result