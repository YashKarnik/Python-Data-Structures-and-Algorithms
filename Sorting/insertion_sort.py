def insertion_sort(a):
    n=len(a)
    j=0
    for i in range(1,n):
        curr=a[i]
        j=i-1
        while(j>=0 and curr<a[j]):
            a[j+1]=a[j]
            j-=1
        a[j+1]=curr
if __name__ == '__main__':
    a=[8,2,4,1,3]
    print(insertion_sort(a))
    print(a)