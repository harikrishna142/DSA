class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)//2
        f=defaultdict(int)
        for i in nums:
            f[i]+=1
            if f[i]>n:
                return i
        return i