class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res=[]
        #com=[]

        def back(i,com):
            if "".join(com)==s:
                res.append(" ".join(com))
                return
            for j in range(len(wordDict)):
                if not s.startswith("".join(com)):
                    return
                
                com.append(wordDict[j])
                back(j,com)
                com.pop()



        back(0,[])
        return res
        