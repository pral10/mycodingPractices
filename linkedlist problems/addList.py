# Write a function, add_lists, that takes in the head of two linked lists, each representing a number.
# The nodes of the linked lists contain digits as values. The nodes in the input lists are reversed;
# this means that the least significant digit of the number is the head. The function should return
# the head of a new linked listed representing the sum of the input lists.
# The output list should have its digits reversed as well.

# You must do this by traversing through the linked lists once.

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def add_lists(head1, head2):
    final = Node(None)
    working = final
    current1 = head1
    current2 = head2
    carry = 0

    while current1 is not None or current2 is not None or carry == 1:
        if current1 is None:
            val1 = 0
        else:
            val1 = current1.val
        if current2 is None:
            val2 = 0
        else:
            val2 = current2.val
        total = val1 + val2 + carry
        if total > 9:
            carry = 1
        else:
            carry =  0
        digit = total % 10
        working.next = Node(digit)
        working = working.next

        if current1 is not None:
            current1 = current1.next
        if current2 is not None:
            current2 = current2.next

    return final.next





def main():
    #   621
    # + 354
    # -----
    #   975

    a1 = Node(1)
    a2 = Node(2)
    a3 = Node(6)
    a1.next = a2
    a2.next = a3
    # 1 -> 2 -> 6

    b1 = Node(4)
    b2 = Node(5)
    b3 = Node(3)
    b1.next = b2
    b2.next = b3
    # 4 -> 5 -> 3

    lol = add_lists(a1, b1)
    while lol is not None:
        print(lol.val)
        lol = lol.next
    # 5 -> 7 -> 9
if __name__ == "__main__":
    main()