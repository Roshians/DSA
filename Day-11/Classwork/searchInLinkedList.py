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

def searchInLinkedList(head, key):
    count = 0
    while head is not None:
        if head.data == key:
            
            return True, count
        head = head.next
        count += 1
    return False

print(searchInLinkedList(first, 20))