class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        st=[]
        for i in range(len(arr)):
            if not st or st[-1]<=arr[i]:
                st.append(arr[i])
            else:
                e=st[-1]
                while st and st[-1]>arr[i]:
                    st.pop()
                st.append(e)
        return len(st)
        


        

        