#Max cibsecutive ones
def findMaxConsecutiveOnes(nums):
        max_count=0
        current_count=0

        for i in nums:
            if i==1:
                current_count+=1
                if current_count>max_count:
                    max_count=current_count
            else:
                current_count=0
        return max_count
        
        for i in nums:
            if i==1:
                current_count+=1
            else:
                max_count=max(max_count, current_count)
                current_count=0
            max_count=max(max_count, current_count)
        return max_count

nums=[1,1,0,1,1,1]
print(findMaxConsecutiveOnes(nums))