class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        print(points)
        i=0
        r=1
        mi=points[0][0]
        ma=points[0][1]
        while i<len(points)-1:
            if max(mi,points[i+1][0])<=min(ma,points[i+1][1]):
                mi=max(mi,points[i+1][0])
                ma=min(ma,points[i+1][1])
                i+=1
            else:
                r+=1
                i+=1
                mi=points[i][0]
                ma=points[i][1]
        return r
            


            
            

        