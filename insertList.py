# Write a function, insert_node, that takes in the head of a linked list, a value, and an index.
# The function should insert a new node with the value into the list at the specified index.
# Consider the head of the linked list as index 0. The function should return the head of the resulting linked list.

# Do this in-place.

# You may assume that the input list is non-empty and the index is not greater than the length of the input list.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def insert_node(head, val, index):
    current = head
    count = 1

    while current is not None:
        if count == index:
            temp = current.next
            current.next = Node(val)
            current.next.next = temp

        count += 1
        current = current.next



    return  head

def main():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d

    lol = insert_node(a, 'v', 3)
    while lol is not None:
        print(lol.val)
        lol = lol.next
    # a -> b -> c -> v -> d

if __name__ == "__main__" :
    main()