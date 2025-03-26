class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp=[0]*len(nums)
        dp[0]=nums[0]
        if len(nums)<=1:
            return True
        if dp[0]==0:
            return False
        for i in range(1,len(nums)):
            dp[i]=max(nums[i],dp[i-1]-1)
            if i<len(nums)-1 and dp[i]<1:
                return False
        
        if dp[-2]>0:
            return True
        else:
            return False

                

        
       


