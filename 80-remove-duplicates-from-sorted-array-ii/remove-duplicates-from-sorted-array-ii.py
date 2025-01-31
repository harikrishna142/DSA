class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        j=1
        while j<len(nums):
            if i==1:
                if nums[j]==nums[j-1]:
                    i=i+1
                    j=j+1
                    continue
            if nums[j]!=nums[j-1]:
                nums[i]=nums[j]
                i=i+1
                if j<len(nums)-1 and nums[j]==nums[j+1]:
                    nums[i]=nums[j+1]
                    i=i+1
                    j=j+1
            j=j+1
        return i

        