class Solution:
    def partitionString(self, s: str) -> int:
        l=[]
        c=1
        for i in range(len(s)):
            if s[i] in l:
                c+=1
                l=[]
                l.append(s[i])
            else:
                l.append(s[i])
        return c
