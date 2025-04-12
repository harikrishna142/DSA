class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr)==1:
            return 1
        m=0
        cn=2
        c=1
        if arr[0]<arr[1]:
            c=0
        elif arr[0]>arr[1]:
            c=1
        else:
            c=2
            cn=1
        for i in range(1,len(arr)-1):
            if (arr[i]>arr[i+1] and c==0) or (arr[i]<arr[i+1] and c==1) and c!=2:
                c=(c+1)%2
                cn+=1
            else: 
                if arr[i]==arr[i+1]:
                    c=2
                    cn=1
                else:
                    if arr[i]<arr[i+1]:
                        c=0
                    elif arr[i]>arr[i+1]:
                        c=1
                    cn=2
            m=max(m,cn)
        return max(m,cn)




