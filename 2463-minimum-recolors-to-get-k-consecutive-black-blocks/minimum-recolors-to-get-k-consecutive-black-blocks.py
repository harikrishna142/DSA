class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        m=mi=blocks[:k].count("W")
        i=1
        j=k
        while j<len(blocks):
            if blocks[i-1]=="W":
                m-=1
            if blocks[j]=="W":
                m+=1
            mi=min(mi,m)
            i+=1
            j+=1
        return mi
    


        