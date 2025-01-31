class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s={}
        for i in nums:
            if i not in s:
                s[i]=1
            else:
                s[i]+=1
        return max(s, key=s.get)
        