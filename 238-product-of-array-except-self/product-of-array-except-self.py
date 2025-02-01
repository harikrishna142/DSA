class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        
        l=[1]*n
        r=[1]*n
        answer=[]
        for i in range(1,len(nums)):
            l[i]=l[i-1]*nums[i-1]
            r[n-1-i]=r[n-i]*nums[n-i]
        print(r)
        print(l)
        for j in range(len(nums)):
            answer.append(l[j]*r[j])
        return answer

        