class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        k=0
        
        while i!=len(nums) and nums[i]!="_":
            if nums[i]==val:
                nums.pop(i)
                nums.append("_")
            else:
                k=k+1
                i=i+1
        return k


        