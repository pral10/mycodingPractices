# create linked list
# Write a function, create_linked_list, that takes in a list of values as an argument.
# The function should create a linked list containing each item of the list as
# the values of the nodes. The function should return the head of the linked list.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
def create_linked_list(arr):
    head = Node(None)
    temp = head
    for val in arr:
        temp.next = Node(val)
        temp = temp.next
    return  head.next
def main():
    lol =create_linked_list(["h", "e", "y", "h", "z"])
    while lol is not None:
        print(lol.val)
        lol = lol.next
if __name__ == "__main__" :
    main()