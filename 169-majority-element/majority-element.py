class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        f=defaultdict(int)
        for i in nums:
            f[i]+=1
        f=dict(sorted(f.items(), key=lambda x:x[1], reverse=True))
        l=list(f.keys())
        return l[0]