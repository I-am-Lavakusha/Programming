# sum of numbers
scores=[67,56,88,99,56,45,67]
print(sum(scores))
sum1=0
for score in scores:
  sum1+=score
print(sum1)

print(max(scores))
max1=-1
for score in scores:
  if score>max1:
    max1=score
print(max1)

print(50*101)
sum2=0
for i in range(1,101):
  sum2+=i
print(sum2)