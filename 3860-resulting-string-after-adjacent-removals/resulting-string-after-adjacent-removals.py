class Solution:
    def resultingString(self, s: str) -> str:
        i=0
        while i<len(s)-1:
            if abs(ord(s[i])-ord(s[i+1])) in [1,25]:
                if i==len(s)-2:
                    s=s[:i]
                else:
                    s=s[:i]+s[i+2:]
                    
                if i!=0:
                    i=i-1
            else:
                i=i+1
        return s

        