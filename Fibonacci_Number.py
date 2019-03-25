    def fib(N):
        if N==1:
            return 1
        elif N==0:
            return 0
        n1,n2 = 0,1
        
        for i in range(N):
           
            n1,n2 = n2,n1+n2
        return n1
print(fib(6))     
