def Merge(a,b):
    n=len(a)
    m=len(b)
    i=0
    j=0
    res=[]
    while(n>0 and m>0):
        if(a[i]<b[i]):
            res.append(a.pop(0))
            n-=1
        else: 
            res.append(b.pop(0))
            m-=1
    while(n>0):
        res.append(a.pop(0))
        n-=1
    while(m>0):
        res.append(b.pop(0))
        m-=1
    return res
    
def MergeSort(a):
    l=len(a)
    if(l>1):
        m=l//2
        leftArr=MergeSort(a[:m])
        rightArr=MergeSort(a[m:])
        SortedArr=Merge(leftArr,rightArr)
        return SortedArr
    return a

if __name__ == '__main__':
    x=MergeSort([9,8,7,6,5,4,3,2,1])
    print(x)
    
