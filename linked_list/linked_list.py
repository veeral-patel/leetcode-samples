class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def length(node):
    if not node:
        return 0
    return 1+length(node.next)

def last(node):
    if not node:
        return None
    elif node and not node.next:
        return node.val
    else:
        return last(node.next)

def middle(node):
    # Get middle by computing length first, then
    # getting the element at index length/2
    size = length(node)
    stop_at = size//2

    for i in range(stop_at):
        node = node.next

    return node.val

empty = None
one = Node(3)
three = Node(3, Node(4, Node(5)))
five = Node(0, Node(1, Node(2, Node(3, Node(4)))))
six = Node(0, Node(1, Node(2, Node(3, Node(4, Node(5))))))

# assert length(empty) == 0
# assert length(one) == 1
# assert length(three) == 3

# assert(last(empty)) == None
# assert(last(one)) == 3
# assert(last(three)) == 5

# print("tests passed")

def middle2(node):
    if not node:
        return None

    slow = node
    fast = node

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow.val
