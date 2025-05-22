class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        c=0
        if tickets[k]==0:
            return 0
        i=0
        while len(tickets)!=0:
            t=tickets.pop(0)
            if t>1:
                tickets.append(t-1)
            else:
                if k==0:
                    c+=1
                    break
            if k==0:
                k=len(tickets)-1
            else:
                k-=1
            c+=1
        return c
            