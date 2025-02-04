class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        r=[]
        k=0
        for i in tokens:
            k=0
            if i=="*":
                k=r[-1]*r[-2]
                if r:
                    r.pop()
                if r:
                    r.pop()
                r.append(k)
            elif i=="+":
                k=r[-1]+r[-2]
                if r:
                    r.pop()
                if r:
                    r.pop()
                r.append(k)
            elif i=="-":
                k=r[-2]-r[-1]
                if r:
                    r.pop()
                if r:
                    r.pop()
                r.append(k)
            elif i=="/":
                k=int(r[-2]/r[-1])
                if r:
                    r.pop()
                if r:
                    r.pop()
                r.append(k)
            else:
                r.append(int(i))
            
        return r[-1]



        