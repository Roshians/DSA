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


while temp.next is not None:
    print(temp.data, end=" ")
    temp = temp.next


