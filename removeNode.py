# remove node
# Write a function, remove_node, that takes in the head of a linked list and a target value as arguments.
# The function should delete the node containing the target value from the linked list and return the head of the
# resulting linked list. If the target appears multiple times in the linked list
# , only remove the first instance of the target in the list.

# Do this in-place.

#You may assume that the input list is non-empty.

# You may assume that the input list contains the target.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
def remove_node(head, target):
    if head.val == target:
        return head.next
    prev = None
    current = head
    while current is not None:
        if current.val == target:
            prev.next = current.next
        prev = current
        current = current.next





    return head
def main():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    # a -> b -> c -> d -> e -> f

    lol = (remove_node(a, "f"))
    while lol is not None:
        print(lol.val)
        lol = lol.next
    # a -> b -> d -> e -> f
if __name__ == "__main__" :
    main()
