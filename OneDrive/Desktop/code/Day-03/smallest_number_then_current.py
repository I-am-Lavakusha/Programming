#smallenst numbers than the current
def smallerNumbersThanCurrent(nums):
        sorted_list=sorted(nums)
        res={}
        for i, val in enumerate(sorted_list):
            if val not in res:
                res[val]=i
        return [res[num] for num in nums]
        res=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    count+=1
            res.append(count)
        return res
nums=[5,5,1,6,7,8]
print(smallerNumbersThanCurrent(nums))