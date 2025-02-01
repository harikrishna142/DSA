class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        c=-1
        n=len(gas)
        g=0
        j=0
        i=0
        while True:
                g=g+gas[i]
                if cost[i]<=g:
                    if c==-1:
                        c=i
                    elif c==i:
                        return i
                    g=g-cost[i]

                else:
                    c=-1
                    g=0
                    if i==len(gas)-1 or j>len(gas)-1:
                        return -1
                j=j+1
                i=(i+1)%n
    
        