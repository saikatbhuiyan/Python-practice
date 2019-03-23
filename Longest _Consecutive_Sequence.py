
def longestConsecutive(nums):
    s = set()
    a = 0
    
    for e in nums:
        s.add(e)
    
    for i in range(len(nums)):
        
        if (nums[i] - 1) not in s:
            
            j = nums[i]
            while(j in s):
                j += 1
            a = max (a, j - nums[i])
    
    return a

print(longestConsecutive([1, 9, 3, 10, 4, 20, 2]))

