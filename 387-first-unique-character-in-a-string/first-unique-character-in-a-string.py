class Solution:
    def firstUniqChar(self, s: str) -> int:
        f=defaultdict(int)
        for i in range(len(s)):
            f[s[i]]+=1
        if min(f.values())!=1:
            return -1
        for i in range(len(s)):
            if f[s[i]]==1:
                return i
            


            

        