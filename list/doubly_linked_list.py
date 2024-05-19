class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail = None
        self.size = 0

    def insert(self,x):
        n=Node(x)
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n
        self.size += 1


    def insert_begin(self, x):
        n = Node(x)
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            self.head.prev = n
            n.next = self.head
            self.head = n
        self.size += 1

    def search(self,x):
        t = self.head
        while t is not None:
            if t.val == x:
                return t
            t = t.next
        return None

    def insert_at(self,x,idx):
        if idx < self.size and idx >= 0:
            t = self.check(idx)
            if t is not self.head:
                n=Node(x)
                t.prev.next = n
                n.prev = t.prev
                n.next = t
                t.prev = n
                self.size += 1
            elif t == self.head:
                self.insert_begin(x)
        else:
            return False


    def check(self,w):
        t = self.head
        j=0
        while t is not None:
            if w == j:
                return t
            j = j+1
            t = t.next

    def remove(self, z: int):
        t = self.search(z)
        self.remove_node(t)

    def remove_head(self):
        self.remove_node(self.head)

    def remove_tail(self):
        self.remove_node(self.tail)

    def remove_node(self, node: Node):
        if node is None:
            return False
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = self.head.next
            self.head.prev = None
        elif node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.size -= 1



    def display(self):
        t = self.head
        while t is not None:
            print(t.val,end =" ")
            t = t.next
        print()

    def reverse_display(self):
        t = self.tail
        while t is not None:
            print(t.val,end=" ")
            t = t.prev
        print()


l=DoublyLinkedList()
# l.insert(5)
# l.insert(6)
# l.insert(7)

l.insert_begin(9)
l.insert(8)
l.insert(7)
print(l.insert_at(5,-1))
print(l.insert_at(6,3))
# l.insert(9)
l.display()
l.reverse_display()