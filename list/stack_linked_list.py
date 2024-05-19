class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


class Stack:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def push(self,x):
        n = Node(x)
        if self.head is None:
            self.head = n
        else:
            n.next= self.head
            self.head = n
        self.size += 1

    def pop(self):
        if self.head is not None:
            t =self.head
            self.head = self.head.next
            return t.val
        else:
            return False
        self.size -= 1

    def peek(self):
        if self.head is not None:
            return self.head.val
        return False
    def is_empty(self):
        return self.head is None

    # def get_item(self,idx):
    #     if idx >= 0 and idx < self.size:
    #         t = self.head
    #         j = 0
    #         while t is not None:
    #             if idx == j:
    #                 return t.val
    #             j = j + 1
    #             t = t.next


    def display(self):
        t = self.head
        while t is not None:
            print(t.val, end=' ')
            t = t.next
        print()

l=Stack()
l.push(8)
l.push(9)
l.push(10)
print(l.peek())
# print(l.get_item(1))
l.display()

