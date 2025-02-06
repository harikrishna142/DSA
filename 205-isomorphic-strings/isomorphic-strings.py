class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        f={}
        for i in range(len(s)):
            if s[i] not in f:
                if t[i] in f.values():
                    return False
                f[s[i]]=t[i]
            else:
                if f[s[i]]!=t[i]:
                    return False
        return True
        