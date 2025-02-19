class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        f=defaultdict(int)
        for i in range(len(s1)):
            f[s1[i]]+=1
        n=len(s2)
        k=len(s1)
        i=0
        l=list(s1)

        while i<n:
            if s2[i] in l and Counter(s2[i:i+k])==f:
                return True
            i+=1
        return False
            
            

        