class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        r=0
        m=0
        for i in range(len(arr)):
            m=max(m,arr[i])
            if m==i:
                r+=1
        return r
        