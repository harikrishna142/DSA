class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        f={}
        c=0
        for i in rectangles:
            if i[0]/i[1] in f:
                f[i[0]/i[1]]=[f[i[0]/i[1]][0]+1,sum(f[i[0]/i[1]])]
            else:
                f[i[0]/i[1]]=[1,0]
        for x in f.values():
            c=c+x[1]
        return c



        