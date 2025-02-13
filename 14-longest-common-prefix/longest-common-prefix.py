class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r=min(len(i) for i in strs)
        s=strs[0]
        s1=s[:r]
        for i in range(1,len(strs)):
            for j in range(len(s1)):
                if s1[j]!=strs[i][j]:
                    s1=s1[:j]
                    break
        return s1       


