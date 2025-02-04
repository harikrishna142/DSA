class Solution:
    def isValid(self, s: str) -> bool:
        f={"}":"{","]":"[",")":"("}
        r=[]
        for i in range(len(s)):
            if s[i] in f:
                if len(r)==0 or f[s[i]]!=r[-1]:
                    return False
                elif f[s[i]]==r[-1]:
                    r.pop()
            else:
                r.append(s[i])
        return len(r)==0
        
                    


        