class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def insert(self,x):
        n = Node(x)
        if self.head is None:
            self.head = n
        else:
            t = self.head
            while t.next is not None:
                t=t.next
            t.next = n

    def insert_begin(self,x):
        n=Node(x)
        n.next = self.head
        self.head = n



    def size(self):
        j=0
        t = self.head
        while t is not None:
            j = j+1
            t = t.next
        return j

    def search(self,x):
        j=0
        t = self.head
        while t is not None:
            if t.val == x:
                return j
            t = t.next
            j += 1
        return -1

    def remove(self,x):
        t, p = self.head, None
        while t is not None:
            if t.val == x:
                if p is None:
                    self.head = self.head.next
                else:
                    p.next = p.next.next
                return
            p = t
            t = t.next

    def display(self):
        t = self.head
        while t is not None:
            print(t.val,end=' ')
            t = t.next
        print()

l=LinkedList()
l.insert(5)
l.insert(4)
l.insert(4)
l.insert(6)
l.insert(1)
print(l.size())
print(l.search(7))
l.insert_begin(8)
l.remove(5)
l.remove(4)
# l.remove(1)
l.display()








