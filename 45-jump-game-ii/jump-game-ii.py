class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        
        j=0
        c=0
        f=0
        for i in range(n-1):
            f=max(f,i+nums[i])
            if i==c:
                j+=1
                c=f
        return j



       
    
