class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        i=0
        c=customers[0][0]
        w=0
        while i<len(customers):
            c=max(c,customers[i][0])+customers[i][1]
            w=w+(c-customers[i][0])
            i+=1
        return float(w/len(customers))


        