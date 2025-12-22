#Concatanation of Array
def getConcatenation(nums):
    return nums + nums
    return nums*2
    nums.extend(nums)
    return nums
nums=[1,2,3]
print(getConcatenation(nums))