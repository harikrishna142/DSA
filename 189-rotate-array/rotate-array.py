class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        i=0
        j=len(nums)-1
        p=0
        while i<k:
            p=nums.pop(j)
            nums.insert(0,p)

            i=i+1
        return nums
        """
        Do not return anything, modify nums in-place instead.
        """
        