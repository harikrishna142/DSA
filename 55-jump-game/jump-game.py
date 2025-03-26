class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end=nums[0]
        if len(nums)==1:
            return True
        for i in range(1,len(nums)-1):
            if end<i:
                return False
            end=max(end,i+nums[i])
            if end>=len(nums)-1:
                return True
        if end>=len(nums)-1:
            return True
        return False


                

        
       


