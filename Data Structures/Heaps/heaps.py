class heap:
    def __init__(self,reverse=False):
        self.comparator=lambda a,b: bool(a<b) if(reverse) else bool(a>b)
        self.heap=[]
        
        
    def insert(self,value):
        self.heap.append(value)
        curr=len(self.heap)-1 #inserted Node
        parent=(curr//2)-1
        self.build_heap()
    
    def delete(self):
        n=len(self.heap)
        self.heap[0],self.heap[n-1]=self.heap[n-1],self.heap[0]
        val=self.heap.pop(-1)
        n-=1
        self.build_heap()
        return val
        
    
    def heapify(self,n,i):
        largest=i
        l=2*i+1
        r=2*i+2
        if(l<n and self.comparator(self.heap[l],self.heap[largest])):
            largest=l
        if(r<n and self.comparator(self.heap[r],self.heap[largest])):
            largest=r
        if(largest!=i):
            self.heap[largest],self.heap[i]=self.heap[i],self.heap[largest]
            self.heapify(n,largest)
            
            
    def build_heap(self):
        n=len(self.heap)
        for i in range(n//2-1,-1,-1):
            self.heapify(n,i)
        
    def isempty(self):
        return not bool(len(self.heap))
        
    def __repr__(self):
        return 'heap({})'.format(self.heap)
    
if __name__ == '__main__':
    # x=heap([1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17],reverse=True)
    x=heap(reverse=False)
    x.insert(9)
    x.insert(7)
    x.insert(19)
    x.insert(1)
    x.insert(10.6)
    x.insert(11.6)
    print(x)
    while(not x.isempty()):
        print(x.delete())
    
    
    
    
