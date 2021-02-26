class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class Sll:
    
    def __init__(self):
        self.head = Node()

    def append(self, x):
        curr = self.head
        if(curr.data == None):
            self.head = Node(x)
        else:
            new_node = Node(x)
            while(curr.next != None):
                curr = curr.next
            curr.next = new_node

    def __repr__(self):
        curr = self.head
        while(curr):
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def deleteNode(self, position):
        curr = self.head
        for _ in range(position):
            curr = curr.next
        x = curr.next.data
        curr.next = curr.next.next
        return x

    def __len__(self):
        c = self.head
        l = 0
        while(c != None):
            l += 1
            c = c.next
        return l

    def reverseList(self):
        x = None
        y = self.head
        while(y != None):
            z = y.next
            y.next = x
            x = y
            y = z
        self.head = x

    def compareLists(self, l):
        c1 = self.head
        c2 = l.head
        while((c1 != None and c2 != None) and c1.data == c2.data):
            c1 = c1.next
            c2 = c2.next
        return (c1 == c2)

    def mergeListandSort(self, l):
        c1 = self.head
        while(c1.next != None):
            c1 = c1.next
        c1.next = l.head
        c1 = self.head
        x = []
        while(c1 != None):
            x.append(c1.data)
            c1 = c1.next
        x.sort()
        n = len(x)
        l3 = Sll()
        for i in range(n):
            l3.append(x[i])
        self.head = l3.head

    def getNode(self, positionFromTail):
        c = self.head
        pos = 0
        while(c != None):
            c = c.next
            pos += 1
        pos = pos-positionFromTail-1
        c = self.head
        for i in range(pos):
            c = c.next
        return (c.data)

    def removeDuplicatesFromSortedList(self):
        c = self.head
        while(c.next != None):
            if(c.data != c.next.data):
                c = c.next
            else:
                c.next = c.next.next

    def hasCycle(self):
        i = self.head
        if(i.next == None or i == None):
            return False
        else:
            j = i.next
            while(j.next != None and j.next.next != None):
                j = j.next.next
                i = i.next
                if(i == j):
                    return True
            return False

    def findMergeNode(self, head2):
        pass


if __name__ == '__main__':
    h1 = Sll()
    h1.append(1)
    h1.append(2)
    h1.append(3)
    h1.append(4)
    h1.append(5)
    h1.append(6)
    h2 = Sll()
    h2.append(11)
    h2.append(22)
    c = h2.head
    h2.head.next.next = h1.head.next.next.next
    h1.printList()
    h2.printList()
