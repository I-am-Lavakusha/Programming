#Set Mismatch
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counts=[0]*(len(nums)+1)
        for i in nums:
            counts[i]+=1
        
        duplicate=-1
        missing=-1
        for i in range(1,len(counts)):
            if counts[i]==2:
                duplicate=i
            elif counts[i]==0:
                missing=i
        return [duplicate, missing]

        n=len(nums)
        e_sum=n*(n+1)//2
        a_sum=sum(nums)
        s_sum=sum(set(nums))

        duplicate=a_sum-s_sum
        missing=e_sum-s_sum
        return[duplicate, missing]