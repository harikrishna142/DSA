class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i=0
        k=0
        j=0
        n=len(nums)
        while j<n:
            if nums[i]==0:
                k=nums.pop(i)
                nums.insert(0,k)
                i=i+1
            elif nums[i]==2:
                k=nums.pop(i)
                nums.append(k)
            else:
                i+=1
            j+=1
    
            

        """
        Do not return anything, modify nums in-place instead.
        """
        