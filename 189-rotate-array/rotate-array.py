class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        r=[0]*len(nums)
        n=len(nums)
        for i in range(len(nums)):
            r[(i+k)%n]=nums[i]
        for i in range(n):
            nums[i]=r[i]
        
        """
        Do not return anything, modify nums in-place instead.
        """
        