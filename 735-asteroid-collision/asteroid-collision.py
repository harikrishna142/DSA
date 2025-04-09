class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s=[]
        for i in range(len(asteroids)):
            s.append(asteroids[i])
            while s and s[-1]<0:
                if len(s)==1 or (s[-2]<0):
                    break
                if (s[-2])>abs(s[-1]):
                    s.pop()
                
                elif (s[-2])<abs(s[-1]):
                    k=s.pop()
                    s.pop()
                    s.append(k)
                else:
                    s.pop()
                    s.pop()
        return s


