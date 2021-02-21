from binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    def __init__(self, data=None):
        self.root = Node(data)

    def insert(self, value=None):
        if(value is None):
            return 'Cannot insert null node'
        newNode = Node(value)
        newNode.height = 0
        if(self.root.data is None):
            self.root = newNode
            return
        curr = self.root
        prev = None
        while(curr is not None):
            prev = curr
            if(value > curr.data):
                curr = curr.right
            else:
                curr = curr.left
        if(value > prev.data):
            prev.right = newNode
        else:
            prev.left = newNode
        super().height()
        return newNode

    def copy(self):
        newTree = BinarySearchTree()
        arr = super().levelOrderTraversal()
        for i in arr:
            if(i == '\n'):
                continue
            newTree.insert(i.data)
        return newTree


if __name__ == '__main__':
    x = BinarySearchTree()
    x.insert(7)
    x.insert(3)
    x.insert(1)
    x.insert(2)
    x.insert(4)
    x.insert(5)

    T = BinarySearchTree()
    for i in range(1, 15):
        T.insert(i)
    print(T)
