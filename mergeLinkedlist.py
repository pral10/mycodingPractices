#Write a function, merge_lists, that takes in the head of two sorted linked lists as arguments.
# The function should merge the two lists together into single sorted linked list.
# The function should return the head of the merged linked list.

# Do this in-place, by mutating the original Nodes.

# You may assume that both input lists are non-empty and contain increasing sorted numbers.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def merge_lists(head1, head2):
    list3 = Node(None)
    list4 = list3
    current1 = head1
    current2 = head2
    while current1 is not None and current2 is not None:
        if current1.val < current2.val:
            list4.next = current1
            current1 = current1.next
        else:
            list4.next = current2
            current2 = current2.next
        list4 = list4.next
    if current1 is not None:
            list4.next = current1
    if current2 is not None:
            list4.next = current2
    return list3.next
def main():
    a = Node(5)
    b = Node(7)
    c = Node(10)
    d = Node(12)
    e = Node(20)
    f = Node(28)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    # 5 -> 7 -> 10 -> 12 -> 20 -> 28

    q = Node(6)
    r = Node(8)
    s = Node(9)
    t = Node(25)
    q.next = r
    r.next = s
    s.next = t
    # 6 -> 8 -> 9 -> 25

    lol = (merge_lists(a, q))
    while lol is not None:
        print (lol.val)
        lol = lol.next
    # 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 12 -> 20 -> 25 -> 28
if __name__ == "__main__":
    main()

