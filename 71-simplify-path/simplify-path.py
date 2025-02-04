class Solution:
    import re
    def simplifyPath(self, path: str) -> str:
        r=re.split(r'[/]',path)
        l=[]
        print(l)
       
        for i in r:
            if i=="." or i=="":
                continue
            elif i=="..":
                l=l[:-1]
                l=l[:-1]
            else:
                l.append("/")
                l.append(i)
        l="".join(l)
        if len(l)==0:
            return "/"
        return "".join(l)
        
        return l


        


                        
                    
                
            

