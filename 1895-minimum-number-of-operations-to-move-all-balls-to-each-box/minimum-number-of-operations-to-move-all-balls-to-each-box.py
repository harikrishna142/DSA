class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        c=0
        c1=0
        n=len(boxes)-1
        l=[0]*len(boxes)
        r=[0]*len(boxes)
        for i in range(len(boxes)-2,-1,-1):
            l[i]=l[i+1]+c+int(boxes[i+1])
            r[n-i]=r[n-i-1]+c1+int(boxes[n-i-1])
            if boxes[i+1]=="1":
                c+=1
            if boxes[n-i-1]=="1":
                c1+=1
        for i in range(len(boxes)):
            l[i]+=r[i]
        return l
        

        