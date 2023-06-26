# is univalue list
# Write a function, is_univalue_list, that takes in the head of a linked list as an argument.
# The function should return a
# boolean indicating whether or not the linked list contains exactly one unique value.

# You may assume that the input list is non-empty.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def is_univalue_list(head):
    val = head.val
    current = head
    while current is not None:
        if current.val != val:
            return False
        current =current.next
    return True

def recursive (head, prev = None):
    if head is None:
        return None
    if prev is None or  head.val == prev:
        return recursive(head.next, prev= head.val)
    return False





def main():
    u = Node(2)
    v = Node(2)
    w = Node(2)
    x = Node(2)
    y = Node(2)

    u.next = v
    v.next = w
    w.next = x
    x.next = y

    # 2 -> 2 -> 2 -> 2 -> 2

    print(is_univalue_list(u))  # True
if __name__ == "__main__":
    main()