class Solution:
    def mySqrt(self, x: int) -> int:
        if x in [1,2,3]:
            return 1
        j=x//2
        i=0
        m=i+(j-i)//2
        while i<=j:
            if m*m>x:
                j=int(m)-1
            elif m*m<x:
                i=int(m)+1
            else:
                return int(m)
            m=i+(j-i)//2
        return int(m)        