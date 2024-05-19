import array
import ctypes
class Stack:
    def __init__(self, capacity):
        self._capacity = capacity
        self._i = 0
        self._arr = (self._capacity * ctypes.py_object)()

    def push(self,x):
        if not self.is_full():
            self._arr[self._i] = x
            self._i += 1
            return True


    def pop(self):
        if self.is_empty:
            t= self._arr[self._i -1]
            self._i -= 1
            return t

    def peek(self):
        if self.is_empty:
             return self._arr[self._i -1]
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

l = Stack(4)
print(l.is_empty())
print(l.push(5))
print(l.push(3))
print(l.push(2))
print(l.pop())
print(l.size())
l.display()