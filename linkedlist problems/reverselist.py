# reverse list
# Write a function, reverse_list, that takes in the head of a linked list as an argument. The function should reverse the order of the nodes in the linked list in-place and return the new head of the reversed linked list.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# a -> b -> c-> d 

def reverse_list(head):
    prev = None # prev pointing to none
    current = head # c
    while current is not None:
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode
    return prev.val


def main():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')

    a.next = b
    b.next = c
    c.next = d
    d.next = None

    print(reverse_list(a))
    

if __name__ == "__main__":
    main()
