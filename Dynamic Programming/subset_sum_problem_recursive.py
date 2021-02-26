# return a boolean if a target sum can be achieve from an array of integers
def can_sum(a,target,memo={}):
    if(memo.get(target)):return memo[target]
    if(target==0):  return True
    elif(target<0): return False
    else:
        for i in a:
            if(can_sum(a,target-i)==True):
                memo[target]=True
                return True
        memo[target]=False
        return False
    
if __name__ == '__main__':
    print(can_sum([2,3,4,7],7))
    print(can_sum([3, 34, 4, 12, 5, 2],9))
