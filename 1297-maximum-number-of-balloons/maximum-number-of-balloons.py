class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        f={}
        p=["b","a","l","o","n"]
        for i in p:
            f[i]=0
        for i in range(len(text)):
            if text[i] in p:
                f[text[i]]+=1
        return min(min(f.values()),int((min(f["l"],f["o"]))//2))




        