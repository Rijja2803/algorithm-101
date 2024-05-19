import array


class List:
    def __init__(self, capacity):
        self._capacity = capacity
        self._i = 0
        self._arr = array.array('i', [0] * capacity)

    def insert(self, x):
        if not self.is_full():
            self._arr[self._i] = x
            self._i += 1
            return True
        return False

    def insert_at_beginning(self, x):
        if self._i < self._capacity:
            for j in range(self._i, 0, - 1):
                self._arr[j] = self._arr[j-1]
            self._arr[0] = x
            self._i += 1
            return True
        return False

    def insert_at(self,idx,w):
        if idx < 0 or idx >= self._i:
            return False
        if self._i < self._capacity:
            for j in range (self._i, idx, -1):
                self._arr[j] = self._arr[j-1]
            self._arr[idx] = w
            self._i += 1
            return True
        return False

    def get_ele(self,x):
        if x>=0 and x< self._capacity:
            return self._arr[x]


    def search(self, y) -> int:
        for i in range(self._i):
            if self._arr[i] == y:
                return i
        return -1

    def remove(self, z) -> bool:
        t = self.search(z)
        if t == -1:
            return False
        for i in range(t, self._i - 1):
            self._arr[i] = self._arr[i + 1]
        self._i -= 1
        return True

    def remove_at(self,idx):
        if idx < 0 or idx >= self._i:
            return False
        if self._i > 0:
            for i in range(idx, self._i - 1):
                self._arr[i] = self._arr[i + 1]
            self._i -= 1
            return True

    def remove_at_beginning(self):
        for i in range(0, self._i-1):
            self._arr[i] = self._arr[i + 1]
        self._i -= 1

    def remove_end(self):
        if self._i>0:
            self._arr[self._i] = 0
            self._i -= 1

    def size(self):
        return self._i
    def is_empty(self):
        if self._i == 0:
            return True
        return False
    def is_full(self):
        if self._i == self._capacity:
            return True
        return False

    def display(self):
        for i in range(self._i):
            print(self._arr[i], end=' ')
        print()


l = List(4)
print(l.is_empty())
print(l.insert(1))
print(l.insert(3))
print(l.insert_at_beginning(5))
print(l.size())
print(l.insert_at(1,4))
print(l.is_full())
#print(l.remove_at_beginning())
##print(l.remove_end())
#print(l.insert(3))
print(l.remove_at(1))
print(l.get_ele(2))


# print(l.search(1))
# print(l.search(7))
#
# print(l.remove(1))
# l.display()

#print(l.remove(1))
# l.display()
#
# print(l.remove(3))
# l.display()
#
# print(l.remove(4))
# l.display()
#
# print(l.insert(11))
# print(l.insert(12))
# print(l.insert(13))
# print(l.insert(14))
#
l.display()
