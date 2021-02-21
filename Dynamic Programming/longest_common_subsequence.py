from collections import deque
def commonChild(s1, s2):
    n=len(s1)
    m=len(s2) 
    T=[[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(s1[i-1]==s2[j-1]):
                T[i][j]=1+T[i-1][j-1]
            else:
                T[i][j]=max(T[i-1][j],T[i][j-1])
    res=deque()
    i=n # Number of rows (index)
    j=m # Column number (index)
    while(i>0 and j>0):
        if(T[i][j]==T[i][j-1]):
            j-=1
        else:
            res.appendleft(s2[j-1])
            i-=1
            j-=1
    return T[n][n],''.join(res)


if __name__ == '__main__':
    print(commonChild('SHINCHAN','NOHARAAA'))
    print(commonChild('STONE','LONGEST'))
    print(commonChild('HARRY','SALLY'))