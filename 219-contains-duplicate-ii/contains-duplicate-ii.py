class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        f={}
        for i in range(len(nums)):
            if nums[i] in f and abs(f[nums[i]]-i)<=k:
                    return True
            else:
                f[nums[i]]=i
        return False

        
        