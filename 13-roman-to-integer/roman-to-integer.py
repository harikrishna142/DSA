class Solution:
    def romanToInt(self, s: str) -> int:
        p={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        r=0
        i=len(s)-1
        r+=p[s[i]]
        i=i-1
        
        while i>=0:
            if p[s[i]]<p[s[i+1]]:
                r=r-p[s[i]]
            else:
                r+=p[s[i]]
            i=i-1
        return r








        