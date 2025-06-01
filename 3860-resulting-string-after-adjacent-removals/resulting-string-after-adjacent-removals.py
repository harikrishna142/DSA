class Solution:
    def resultingString(self, s: str) -> str:
        st=[s[0]]
        for i in range(1,len(s)):
            if len(st)==0 or abs(ord(s[i])-ord(st[-1])) not in [1,25]:
                st.append(s[i])
            else:
                st.pop()   
        return "".join(st)

        