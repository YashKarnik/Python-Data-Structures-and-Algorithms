def QuickSort(a):
    n = len(a)
    i = 1
    j = n-1

    def partition(l, u):
        pivot = a[l]
        i = l
        j = u
        while(i <= j):
            while(i <= u and a[i] <= pivot):
                i += 1
            while(a[j] > pivot and j >= l):
                j -= 1
            if(i < j):
                a[i], a[j] = a[j], a[i]
        a[l], a[j] = a[j], a[l]
        return j

    def innerRecursive(l, h):
        if(l < h):
            pivotIndex = partition(l, h)
            innerRecursive(l, pivotIndex-1)
            innerRecursive(pivotIndex+1, h)
    innerRecursive(0, n-1)
    return a


if __name__ == '__main__':
    print(QuickSort([30, 35, 10, 15, 20, 34, 5, 18, 6, 11, 13, 26, 38]))
