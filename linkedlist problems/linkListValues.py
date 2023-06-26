# a -> b -> c -> d

# -> [ 'a', 'b', 'c', 'd' ]
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def linked_list_values(head):
    output = []
    current = head
    while current is not None:
        output.append(current.val)
        current = current.next
    return output


def main():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    a.next = b
    b.next = c
    c.next = d
    print(linked_list_values(a))


if __name__ == "__main__":
    main()
