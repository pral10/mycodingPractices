# Write a function, sum_list, that takes in the head of a linked list
#  containing numbers as an argument. The function should return the total sum of all values in the linked list.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def sum_list(head):
    current = head
    total = 0
    while current:
        total += current.val
        current = current.next
    return total

def main():
    a = Node(1)
    b = Node(4)
    c = Node(7)
    d = Node(9)
    
    a.next = b
    b.next = c
    c.next = d

    print(sum_list(a))
    
if __name__ == "__main__":
    main()