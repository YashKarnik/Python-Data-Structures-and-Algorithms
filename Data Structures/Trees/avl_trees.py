from binary_search_tree import BinarySearchTree
from binary_tree import Node as N


class Node(N):
    def __init__(self, data=None):
        super().__init__(data)

    def __repr__(self):
        return 'Data={} | Height={}'.format(self.data, self.height)


class AVLTree(BinarySearchTree):
    def __init__(self, value=None):
        self.root = Node(vaue)

    def insert(self, value):
        # newNode = Node(vaue)
        # if(self.root.data is None):
        #     self.root = newNode
        #     return
        # curr = self.root
        # parent = None
        # while(curr is not None):
        #     parent = curr
        #     if(curr.data < value):
        #         curr = curr.right
        #     else:
        #         curr = curr.left
        # if(parent.data > value):
        #     parent.left = newNode
        # else:
        #     parent.right = newNode

        newNode = super().insert(value)
        curr = self.root
        unbalancedNode = None
        parentOfUnbalanced = None
        prev = None
        # find unbalanced nde
        while(curr is not None):
            lh = subtree.left.height if(subtree.left is not None) else 0
            rh = subtree.right.height if(subtree.right is not None) else 0
            bf = abs(lh-rh)
            if(bf > 1):
                parentOfUnbalanced = prev
                unbalancedNode = curr
            if(curr.data < value):
                curr = curr.left
            else:
                curr = curr.right
            prev = curr
        if(unbalancedNode is None):
            return
        midNode = None
        if(unbalanced.data < value):
            midNode = unbalancedNode.right
        else:
            midNode = unbalancedNode.left


if __name__ == '__main__':
    T = AVLTree()
    res = []
    for i in range(1, 11):
        res.append(T.insert(i))
    res.append(T.insert(12))
    for i in res:
        print(i)
