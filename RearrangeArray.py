class Solution:
    def reArrange(self,arr):
        arr.sort()

        n=len(arr)

        #reverse the second half
        arr[n//2:]=reversed(arr[n//2:])

arr=[5,2,9,1,6,3]
sol=Solution()
sol.reArrange(arr)
print(arr)        