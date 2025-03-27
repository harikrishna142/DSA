class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       
        nums.sort()
        if len(nums)<=1:
            return len(nums)
        j=1
        m=0
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            if nums[i]==nums[i-1]+1:
                j=j+1
            else:
                m=max(m,j)
                j=1
        return max(m,j)



