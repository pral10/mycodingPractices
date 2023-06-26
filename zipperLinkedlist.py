# Write a function, zipper_lists, that takes in the head of two linked lists as arguments.
# The function should zipper the two lists together into single linked list by alternating nodes.
# If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes.
# The function should return the head of the zippered linked list.

# Do this in-place, by mutating the original Nodes.

# you may assume that both input lists are non-empty.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def zipper_lists(head1, head2):
    list3 = head1
    current1 = head1.next
    current2 = head2


    count = 0
    while current1 is not None and current2 is not None:
        if count % 2 == 0:
            list3.next = current2
            current2 = current2.next
            #list3 = list3.next
        else:
            list3.next = current1
            current1 = current1.next
           # list3=list3.next
        list3 = list3.next
        count = count+1

    if current1 is not None:
        list3.next = current1
    if current2 is not None:
        list3.next = current2
    current4 = head1
    while current4 is not None:
        print(current4.val)
        current4 = current4.next

    return head1




def main():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    a.next = b
    b.next = c
    # a -> b -> c

    x = Node("x")
    y = Node("y")
    z = Node("z")
    x.next = y
    y.next = z
    # x -> y -> z

    zipper_lists(a, x)
    # a -> x -> b -> y -> c -> z


if __name__ == "__main__":
    main()
