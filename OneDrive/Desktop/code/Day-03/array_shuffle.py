def shuffle(nums, n):
  res=[]
  for i in range(n):
    res.append(nums[i])
    res.append(nums[n])
    n+=1
  return res
  return [nums[i+j] for i in range(n) for j in (0,n)]

nums=[2,5,1,3,4,7]
n=3
print(shuffle(nums, n))