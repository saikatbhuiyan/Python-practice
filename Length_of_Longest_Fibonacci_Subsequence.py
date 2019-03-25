 def lenLongestFibSubseq(A):
        s = set(A)
        maxL = 0
        
        for i in range(0,len(A)):
            for j in range(i+1, len(A)):
                
                x = A[i]
                y = A[i] + A[j]
                
                l = 2
                
                while y in s:
                    z = x + y
                    x = y
                    y = z
                    
                    l  += 1
                    
                    maxL = max(maxL,l)
        return maxL if maxL >= 3 else 0
print(lenLongestFibSubseq([2,4,7,8,9,10,14,15,18,23,32,50]))
