class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        s=[]
        for i in bills:
           
            if i!=20:
                heapq.heappush(s,i)
            if i>5:
                j=i-5
                k=0
                s.sort()
                s=s[::-1]
                while j and k<len(s):
                    if s[k]>j:
                        k+=1
                        continue
                    if s[k]==j:
                        s.remove(s[k])
                        j=0
                        break
                    elif s[k]<j:
                        j-=s[k]
                        s.remove(s[k])
                if j:
                    return False
        return True


                    




        return True

        