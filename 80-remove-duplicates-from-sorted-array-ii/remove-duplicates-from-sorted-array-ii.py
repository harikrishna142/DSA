class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        f=defaultdict(int)
        i=0
        n=len(nums)
        for j in range(n):
            if f[nums[j]]<2:
                f[nums[j]]+=1
                nums[i]=nums[j]
                i+=1
        return i


