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
        return ''

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

    def has_cycle(self):
        hare=self.head
        tortoise=self.head
        while(tortoise is not None):
            tortoise=tortoise.next
            hare=hare.next
            if(hare.next is not None):
                hare=hare.next
            else: break
            if(hare is tortoise):
                return hare
        return None


if __name__ == '__main__':
    h1 = Sll()
    h1.append(1)
    h1.append(2)
    h1.append(3)
    h1.append(4)
    h1.append(5)
    h1.append(6)
    y=h1.getNode(0)
    x=h1.getNode(2)
    y.next=x
    print(h1.has_cycle())
