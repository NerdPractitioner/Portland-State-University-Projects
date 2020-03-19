def has22(nums):
    k=0
    for i in range(len(nums)):
        while k <= len(nums):
            if nums[i] == 2 and nums[i+1] == 2:
                k+=1
                return True
    return False
        
        
        
