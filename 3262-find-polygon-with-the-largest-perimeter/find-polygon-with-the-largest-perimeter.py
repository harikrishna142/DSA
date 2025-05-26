class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        c=nums[0]+nums[1]
        i=2
        r=-1
        while i<len(nums):
            if nums[i]<c:
                r=c+nums[i]
            c+=nums[i]
            i+=1
        return r
        