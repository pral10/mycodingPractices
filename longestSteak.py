
# longest streak
# Write a function, longest_streak, that takes in the head of a linked list as an argument.
# The function should return the length of the longest consecutive streak of the same value within the list.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def longest_streak(head):
    max = 0
    current_max = 0
    prev = None
    current = head
    while current is not None:
        if current.val == prev:
            current_max += 1
        else:
            current_max = 1
        prev = current.val
        if current_max > max:
            max = current_max
        current = current.next




    return max

def main():
    a = Node(5)
    b = Node(5)
    c = Node(7)
    d = Node(7)
    e = Node(7)
    f = Node(6)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    # 5 -> 5 -> 7 -> 7 -> 7 -> 6

    print(longest_streak(a))  # 3
if __name__ == "__main__" :
    main()
