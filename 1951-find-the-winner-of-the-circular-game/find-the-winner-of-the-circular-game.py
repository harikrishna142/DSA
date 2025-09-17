class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l=[]
        for i in range(n):
            l.append(i+1)
        while len(l)>1:
            i=(k-1)%len(l)
            l.remove(l[i])
            l=l[i:]+l[:i]
        return l[0]


        