#finding all the disappeared numbers from 1 to n
def findDisappearedNumbers(num):
        nums_set=set(nums)
        res=[]
        for i in range(1, len(nums)+1):
            if i not in nums_set:
                res.append(i)
        return res
nums=[2,3,4,5,6,7,7,8,8]
print(findDisappearedNumbers(nums))