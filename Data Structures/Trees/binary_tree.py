class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

    def __repr__(self):
        return 'Data={} | Height={}'.format(self.data, self.height)


class BinaryTree:

    def getData(self, node):
        return node.data

    def preorder_traversal(self):
        result = []

        def wrapper(subtree):
            if(subtree is not None):
                result.append(subtree)
                wrapper(subtree.left)
                wrapper(subtree.right)
        if(self.root is None):
            return None
        wrapper(self.root)
        return result

    def inorder_traversal(self):
        result = []

        def wrapper(subtree):
            if(subtree is not None):
                wrapper(subtree.left)
                result.append(subtree)
                wrapper(subtree.right)
        if(self.root is None):
            return None
        wrapper(self.root)
        return result

    def postorder_traversal(self):
        result = []

        def wrapper(subtree):
            if(subtree is not None):
                wrapper(subtree.left)
                wrapper(subtree.right)
                result.append(subtree)
        if(self.root is None):
            return None
        wrapper(self.root)
        return result

    def height(self):
        def wrapper(subtree):
            if(subtree is not None):
                wrapper(subtree.left)
                wrapper(subtree.right)
                lh = 1+subtree.left.height if(subtree.left is not None) else 0
                rh = 1+subtree.right.height if(
                    subtree.right is not None) else 0
                subtree.height = max(lh, rh)
        wrapper(self.root)

    def levelOrderTraversal(self):
        queue = [self.root, None]
        res = []
        while(queue):
            node = queue.pop(0)
            if(node is None):
                if(not queue):
                    break
                res.append('\n')
                queue.append(None)
            else:
                if(node.left is not None):
                    queue.append(node.left)
                if(node.right is not None):
                    queue.append(node.right)
                res.append(node)
        return res

    def verticalTravesal(self):
        d = {}

        def wrapper(subtree, width):
            if(subtree is not None):
                if(d.get(width)):
                    d[width] = d.get(width)+[subtree]
                else:
                    d[width] = [subtree]
                wrapper(subtree.left, width-1)
                wrapper(subtree.right, width+1)
        wrapper(self.root, 0)
        print(d)
        print(sorted(d))

    def invert(self):
        newTree = self.copy()

        def wrapper(subtree):
            if(subtree is not None):
                subtree.left, subtree.right = subtree.right, subtree.left
                wrapper(subtree.left)
                wrapper(subtree.right)
            return subtree
        wrapper(self.root)

    def __repr__(self):
        preorder = list(map(self.getData, self.preorder_traversal()))
        inorder = list(map(self.getData, self.inorder_traversal()))
        postorder = list(map(self.getData, self.postorder_traversal()))
        res = '-'*80
        res += '\nPreorder=>'+str(preorder)
        res += '\nInorder=>'+str(inorder)
        res += '\nPostordr=>'+str(postorder)
        res += '\n'
        res += '-'*80
        return res

    def __len__(self):
        if(self.root.data == None):
            return 0

        def wrapper(subtree):
            if(subtree == None):
                return 0
            return 1+wrapper(subtree.left)+wrapper(subtree.right)
        return wrapper(self.root)


if __name__ == '__main__':
    T = Node(3)
    print(T)
