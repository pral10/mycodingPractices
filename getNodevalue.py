#get node value
#Write a function, get_node_value, that takes in the head of a linked list and an index. The function should return the value of the linked list at the specified index.

# If there is no node at the given index, then return None.

# create a node class
# pass a value
# make connection
# create a function

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
def recursive(head, target, index =0):
    if head is None:
        return -1
    if head.val == target:
        return index
    return recursive(head.next, target , index = index+ 1)
    

def get_node_value(head, target):
    if head is None:
        return None
    index = 0
    current = head
    while current is not None:
        if current.val == target:
            return index
        current = current.next
        index += 1
    return -1


def main():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')

    a.next = b
    b.next = c
    c.next = d
    print(get_node_value(a, 'd'))
    print (recursive(a,'d'))

if __name__ == "__main__":
    main()
