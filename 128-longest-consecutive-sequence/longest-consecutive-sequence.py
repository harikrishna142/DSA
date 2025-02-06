class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        f=defaultdict(int)
        for i in nums:
            if i-1 in f:
                f[i]=f[i-1]+1
            else:
                f[i]=1
        l=list(f.values())
        if len(l)==0:
            return 0
        return max(f.values())

