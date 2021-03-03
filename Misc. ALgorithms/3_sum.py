def threeSum(nums):
    res=[]
    n=len(nums)
    nums.sort()
    for i in range(n):
        if(i>0 and nums[i]==nums[i-1]):
            continue
        left=i+1
        right=n-1
        while(left<right):
            checkSum=nums[left]+nums[right]+nums[i]
            if(checkSum>0):
                right-=1
            elif(checkSum<0):
                left+=1
            else:
                res.append([nums[i],nums[left],nums[right]])
                # print(i,left,right)
                left+=1
                while(nums[left]==nums[left-1] and left<right):
                    left+=1
    return (res)
            
if __name__ == '__main__':
    print(threeSum([-1,0,1,2,-1,-4]))
