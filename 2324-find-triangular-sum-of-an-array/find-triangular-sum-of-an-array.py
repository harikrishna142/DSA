class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums)>1:
            a=[0]*(len(nums)-1)
            for i in range(len(a)):
                a[i]=(nums[i]+nums[i+1])%10
            nums=a
        return nums[-1]
