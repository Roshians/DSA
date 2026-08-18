class node:
    def __init__(self, data):
        self.data = data
        self.next = None

first = node(10)
second = node(20)
third = node(30)
fourth = node(40)

first.next = second
second.next = third
third.next = fourth
temp = first

def newNodeAtLast(head, data):
    curr = head
    while curr.next is not None:
        curr = curr.next

    curr.next = node(data)

    while head.next is not None:
        print(head.data, end=" ")
        head = head.next

newNodeAtLast(temp, 50)