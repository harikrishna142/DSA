class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        s=[]
        if len(nums)==0:
            return nums
        j=nums[0]
        for i in range(len(nums)):
            if i==len(nums)-1:
                if j==nums[i]:
                    s.append(str(j))
                else:
                    s.append(str(j)+"->"+str(nums[i]))

            elif nums[i]+1!=nums[i+1]:
                if j==nums[i]:
                    s.append(str(j))
                else:
                    s.append(str(j)+"->"+str(nums[i]))
                j=nums[i+1]
        return s
            

        

        
        