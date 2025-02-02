class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n=len(s)
        l=numRows+(numRows-2)
        r=""
        if n<3 or numRows==1:
            return s
        j=0
        m=-1
        k=l
        for i in range(numRows):
            if i not in [0,numRows-1]:
                k=k-2
                m=k
            else:
                m=-1
            j=i
            while j<n:
                r+=s[j]
                if j+m<len(s) and m!=-1:
                    r+=s[j+m]
                j=j+l
        return r

        