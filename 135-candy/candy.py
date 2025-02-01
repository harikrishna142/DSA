class Solution:
    def candy(self, ratings: List[int]) -> int:
        r=len(ratings)
        r1=[1]*len(ratings)
        l=0
        m=0
        t=0
        for i in range(len(ratings)):
            t=1
            if i>0 and ratings[i]>ratings[i-1]:
                t=r1[i-1]+1
            if i<len(ratings)-1 and ratings[i]>ratings[i+1]:
                if r1[i+1]+1>t:
                    t=r1[i+1]+1
            r1[i]=t
        
        ratings=ratings[::-1]
        r2=r1
        print(r2)
        r1=[1]*len(ratings)
        for i in range(len(ratings)):
            t=1
            if i>0 and ratings[i]>ratings[i-1]:
                t=r1[i-1]+1
            if i<len(ratings)-1 and ratings[i]>ratings[i+1]:
                if r1[i+1]+1>t:
                    t=r1[i+1]+1
            r1[i]=t
        r1=r1[::-1]
        for i in range(len(ratings)):
            r1[i]=max(r1[i],r2[i])
        return sum(r1)

        
                 

        