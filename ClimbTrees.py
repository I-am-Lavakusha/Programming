def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n
        fib1=1
        fib2=2
        list1=[fib1,fib2]
        for i in range(2,n):
            fib3=fib2+fib1
            list1.append(fib3)
            fib1=fib2
            fib2=fib3
