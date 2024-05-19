import array
import ctypes


class List:
    def __init__(self):
        self._capacity = 4
        self._i = 0
        # self._arr = array.array('i', [0] * self._capacity)
        self._arr = (self._capacity * ctypes.py_object)()

    def insert(self, x):
        if self.is_full():
            self.__resize__()
        self._arr[self._i] = x
        self._i += 1
        return True

    def insert_at_beginning(self, x):
        if self.is_full():
            self.__resize__()

        for j in range(self._i, 0, - 1):
            self._arr[j] = self._arr[j-1]
        self._arr[0] = x
        self._i += 1
        return True

    def insert_at(self,idx,w):
        if idx < 0 or idx >= self._i:
            return False

        if self.is_full():
            self.__resize__()

        for j in range (self._i, idx, -1):
            self._arr[j] = self._arr[j-1]
        self._arr[idx] = w
        self._i += 1
        return True


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

    def __resize__(self):
        print(f'resizing to {self._capacity * 2}')
        new_arr = array.array('i', [0]*(self._capacity *2))
        for i in range(self._capacity):
            new_arr[i] = self._arr[i]
        self._capacity = self._capacity*2
        self._arr = new_arr




    def display(self):
        for i in range(self._i):
            print(self._arr[i], end=' ')
        print()


l = List()
for i in range(1000000000):
    l.insert(i)




# print(l.insert_at_beginning(5))
# print(l.size())
# print(l.insert_at(1,4))
# print(l.is_full())
#print(l.remove_at_beginning())
##print(l.remove_end())
#print(l.insert(3))
#print(l.remove_at(1))


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
# l.display()
