class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        com=[]
        def back(i):
            
            res.append(com[:])
        
            for j in range(i,len(nums)):
                com.append(nums[j])
                back(j+1)
                com.pop()





        back(0)
        return res
        