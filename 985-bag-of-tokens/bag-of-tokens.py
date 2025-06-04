class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        s=0
        i=0
        m=0
        j=len(tokens)-1
        tokens.sort()
        if len(tokens)==0 or power<tokens[0]:
            return 0
        while i<=j:
            if power>=tokens[i]:
                power-=tokens[i]
                s+=1
                m=max(m,s)
                i+=1
            elif s>=1:
                power+=tokens[j]
                s-=1
                j-=1
            else:
                break
        return m

            



        