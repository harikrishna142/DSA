class Solution:
    def trailingZeroes(self, n: int) -> int:
        r=0
        while n>0:
            r+=n//5
            n=n//5
        return r
        