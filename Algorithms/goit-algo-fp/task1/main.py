from classes import Node, LinkedList
from rl import reverse_list
from msl import merge_sorted_lists
from ms import merge_sort 

def main():
    ll = LinkedList()
    ll.append(3)
    ll.append(1)
    ll.append(2)
    ll.append(8)
    ll.append(14)
    ll.append(6)

    # Друк списку
    print("Original list:")
    ll.print_list()

    # Реверсування списку
    reverse_list(ll)
    print("Reversed list:")
    ll.print_list()

    # Сортування списку
    sorted_ll = merge_sort(ll)
    print("Sorted list:")
    sorted_ll.print_list()

    # Об'єднання двох відсортованих списків
    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(6)
    ll1.append(15)
    ll1.append(26)
    ll1.append(30)

    ll2 = LinkedList()
    ll2.append(2)
    ll2.append(4)
    ll2.append(16)
    ll2.append(24)
    ll2.append(77)

    merged_ll = merge_sorted_lists(ll1, ll2)
    print("\nMerged sorted lists:")
    merged_ll.print_list()

if __name__ == "__main__":
    main()

    
