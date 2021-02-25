def heap_sort(a,reverse=False):
    key=lambda a,b: bool(a<b) if(reverse) else bool(a>b)
    n=len(a)
    for i in range(n//2-1,-1,-1):
        heapify(a,n,i,key)
        
    for i in range(n-1,0,-1):
        a[0],a[i]=a[i],a[0]
        heapify(a,i,0,key)
    return a    

def heapify(a,n,i,key):
    largest=i
    left_child=2*i+1
    right_child=2*i+2
    if(left_child<n and key(a[largest],a[left_child])):
        largest=left_child
    if(right_child<n and key(a[largest],a[right_child])):
        largest=right_child
    if(largest!=i):
        a[largest],a[i]=a[i],a[largest]
        heapify(a,n,largest,key)
    else: return 

if __name__ == '__main__':
    x=[19,2,56,8,32,8]
    heap_sort(x,reverse=False)
    print(x)