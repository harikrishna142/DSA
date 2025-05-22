class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i=0
        j=0
        while j<len(s):
            if s[j]==t[i]:
                i+=1
            j+=1
            if i>=len(t):
                return 0
        if i<len(t):
            return len(t)-i
        else:
            return 0
                

        