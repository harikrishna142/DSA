class Solution:
    def canJump(self, nums: List[int]) -> bool:
        g=0
        c=1
        for i in nums:
            if g<0:
                return False
            if i>g:
                g=i
                #c+=1
                #if g>=len(nums)-1:
                    #break
            
            g=g-1
        return True

        

                

        
       


