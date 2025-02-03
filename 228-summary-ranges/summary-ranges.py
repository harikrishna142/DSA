class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        r=[]
        if len(nums)<=0:
            return []
        if len(nums)==1:
            r.append(str(nums[0]))
            return r
        j=nums[0]
        

        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                if j==nums[i-1]:
                    r.append(str(j))
                else:
                    r.append(str(j)+"->"+str(nums[i-1]))
                j=nums[i]
        if j==nums[-1]:
            r.append(str(j))
        else:
            r.append(str(j)+"->"+str(nums[-1]))
        return r

        
        