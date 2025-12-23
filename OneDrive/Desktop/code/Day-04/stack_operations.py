#buiding an array with stack operations
def buildArray(target, n):
        res=[]
        current=0
        for i in range(1, n+1):
            res.append("Push")
            
            if i==target[current]:
                current+=1
            else:
                res.append("Pop")

            if current==len(target):
                break
        return res

target=[1,3]
n=4
print(buildArray(target, n))