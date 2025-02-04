class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i=0
        f=0
        if len(intervals)==0:
            intervals.append(newInterval)
            return intervals
        while i<len(intervals):
            if newInterval[0]>intervals[i][0] and f==0 and len(intervals)==1:
                intervals.append(newInterval)
                f=1
                i+=1
            
            elif newInterval[0]<=intervals[i][0] and f==0:
                if i==0:
                    intervals.insert(i,newInterval)
                    i+=1
                if intervals[i-1][1]>=newInterval[0]:
                    intervals[i-1][1]=max(intervals[i-1][1],newInterval[1])
                else:
                    intervals.insert(i,newInterval)
                    i=i+1
                f=1
            
            elif f==1:
                if intervals[i-1][1]>=intervals[i][0]:
                    intervals[i-1][1]=max(intervals[i-1][1],intervals[i][1])
                    intervals.pop(i)
                else:
                    return intervals
            else:
                i+=1
        if f==0:
            intervals.append(newInterval)
            if intervals[i-1][1]>=intervals[i][0]:
                intervals[i-1][1]=max(intervals[i-1][1],intervals[i][1])
                intervals.pop(i)
        return intervals
            
                


            

        