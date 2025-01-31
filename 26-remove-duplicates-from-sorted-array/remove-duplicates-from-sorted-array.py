class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        i=1
        while i<len(nums):
            if nums[i] in nums[:i]:
                nums.pop(i)
            else:
                i=i+1
        return len(nums)

        