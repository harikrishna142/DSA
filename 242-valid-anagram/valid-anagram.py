class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f1=defaultdict(int)
        f2=defaultdict(int)
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            f1[s[i]]+=1
            f2[t[i]]+=1
        return f1==f2

        
        