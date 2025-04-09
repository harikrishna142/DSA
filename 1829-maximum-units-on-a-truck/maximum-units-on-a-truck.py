class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        b=sorted(boxTypes, key=lambda x:x[1], reverse=True)
        t=truckSize
        
        i=0
        r=0
        while t>0 and i<len(b):
            if b[i][0]<=t:
                t-=b[i][0]
                r+=(b[i][0]*b[i][1])
            else:
                r+=(t*b[i][1])
                t=0
            i+=1
        return r

        print(boxTypes)