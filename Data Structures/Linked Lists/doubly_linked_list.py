class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = Node()

    def append(self, x):
        new_node = Node(x)
        if(self.head.data == None):
            self.head = new_node
        else:
            c = self.head
            while(c.next != None):
                c = c.next
            c.next = new_node
            new_node.prev = c

    def PrintList(self):
        c = self.head
        while(c != None):
            print(c.data)
            c = c.next

    def InsertIntoSorted(self, x):
        new_node = Node(x)
        c = self.head
        while(c != None and x >= c.data):
            c = c.next
        if(c == None):
            a = self.head
            while(a.next != None):
                a = a.next
            a.next = new_node
            new_node.prev = a
        elif(c.prev == None):
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            c.prev.next = new_node
            new_node.prev = c.prev
            new_node.next = c
            c.prev = new_node


if __name__ == "__main__":
    l1 = DLL()
    l1.append(1)
    l1.append(2)
    l1.append(4)

    l1.append(5)
    l1.InsertIntoSorted(0)
    l1.InsertIntoSorted(3)
    l1.InsertIntoSorted(4)
    l1.InsertIntoSorted(6)
    l1.PrintList()
