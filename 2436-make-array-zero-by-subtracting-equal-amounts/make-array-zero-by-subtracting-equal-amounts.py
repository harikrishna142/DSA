class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c=0
        while sum(nums)!=0:
            k=math.inf
            for j in nums:
                if j>0:
                    k=min(k,j)
            
            c+=1
            for i in range(len(nums)):
                if nums[i]>0:
                    nums[i]-=k
        return c

        