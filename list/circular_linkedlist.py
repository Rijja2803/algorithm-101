class Node:
        def __init__(self,val):
            self.val = val
            self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self,x):
        n =Node(x)
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            n.next = self.head
            self.tail = n

    def display(self):
        if self.head is None:
            print('Empty')
        else:
            t = self.head.next
            print(self.head.val,end =" ")
            while t != self.head:
                print(t.val, end = " ")
                t = t.next
        print()

l=CircularLinkedList()
l.insert(5)
l.insert(6)
l.insert(7)
l.insert(8)
l.display()




