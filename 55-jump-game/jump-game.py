class Solution:
    def canJump(self, nums: List[int]) -> bool:
        c=m=nums[0]
        if len(nums)==1:
            return True
        for i in range(len(nums)):
            if nums[i]==0 and m<=i:
                return False
            if i+nums[i]>m:
                c=m=i+nums[i]

            if m>=len(nums)-1:
                return True
        return False

        

                

        
       


