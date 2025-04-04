class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=min(len(i) for i in strs) 
        m=strs[0][:n]
        for i in range(1,len(strs)):
            while m!=strs[i][:n]:
                n=n-1
                if n==0:
                    return ""
                m=m[:n]
                
        return m
            


