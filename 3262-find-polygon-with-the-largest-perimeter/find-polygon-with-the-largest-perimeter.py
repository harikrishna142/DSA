class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        nums=nums[::-1]
        i=0
        while i<len(nums):
            if nums[i]<sum(nums[i+1:]):
                return sum(nums[i:])
            i+=1
        return -1
        