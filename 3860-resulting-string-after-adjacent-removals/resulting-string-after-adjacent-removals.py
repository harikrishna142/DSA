class Solution:
    def resultingString(self, s: str) -> str:
        i=0
        st=[s[0]]
        for i in range(1,len(s)):
            if len(st)==0:
                st.append(s[i])
                continue
            if abs(ord(s[i])-ord(st[-1])) in [1,25]:
                st.pop()
            else:
                st.append(s[i])
            
                
        return "".join(st)

        