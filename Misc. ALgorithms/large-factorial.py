def fact(n):
    res=[None]*10000
    res[0]=1
    q=2
    l=1
    for q in range(2,n+1):
        carry=0
        count=0
        while(count<l):
            res[count]=res[count]*q
            res[count]+=carry
            carry=res[count]//10
            res[count]=res[count]%10
            count+=1
        while(carry!=0):
            res[l]=carry%10
            carry//=10
            l+=1
    return reversed(res[:l])
if __name__ == '__main__':
    res=fact(999)
    for i in res:
        print(i,end='')