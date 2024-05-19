class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self._root = None

    def insert(self, x):
        self._root = self._insert_node(self._root,x)

    def _insert_node(self, n: Node, x: int) -> Node:
        if n is None:
            return Node(x)
        if x< n.val:
            n.left = self._insert_node(n.left,x)
        else:
            n.right = self._insert_node(n.right,x)
        return n

    def inorder(self):
        self._inorder_node(self._root)
        print()

    def _inorder_node(self, n: Node):
        if n is None:
            return
        self._inorder_node(n.left)
        print(n.val, end=" ")
        self._inorder_node(n.right)

    def preorder(self):
        self._preorder_node(self._root)
        print()

    def _preorder_node(self, n: Node):
        if n is None:
            return
        print(n.val, end=" ")
        self._preorder_node(n.left)
        self._preorder_node(n.right)


t = Tree()
t.insert(4)
t.insert(2)
t.insert(5)
t.insert(1)
t.insert(3)
t.insert(6)
t.insert(7)
t.inorder()
t.preorder()
