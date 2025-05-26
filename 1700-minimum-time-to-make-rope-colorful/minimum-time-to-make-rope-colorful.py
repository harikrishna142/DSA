class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        s=[-neededTime[0]]
        i=1
        c=0
        n=len(colors)
        while i<n:
            if colors[i]==colors[i-1]:
                heapq.heappush(s,-neededTime[i])
                if i==n-1:
                    
                    c+=(-sum(s)+heapq.heappop(s))
                    break
            else:
                if len(s)>1:
                    
                    c+=(-sum(s)+heapq.heappop(s))
                s=[]
                heapq.heappush(s,-neededTime[i])
                
            i+=1
        return c



        