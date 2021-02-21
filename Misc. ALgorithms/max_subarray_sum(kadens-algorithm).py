def MaxSumArray(a):
    curr=overall=a[0]
    n=len(a)
    start=end=0
    c=0
    for i in range(1,n):
        if(a[i]<curr+a[i]):
            curr+=a[i]
            c+=1
        else:
            curr=a[i]
            c=0
        if(overall<curr):
            overall=curr
            end=i
            start=end-c
    return overall,start,end
        
if __name__ == '__main__':
    res=MaxSumArray([5,3,-1,6,-14,7,-1])
    print(res)
    res=MaxSumArray([5,3,-1,6,-10])
    print(res)
    res=MaxSumArray([-2, -3, 4, -1, -2, 1, 5, -3])
    print(res)
    res=MaxSumArray([-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7])
    print(res)
