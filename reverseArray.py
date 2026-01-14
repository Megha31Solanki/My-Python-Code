class Solution:
    def reverseArray(self,arr):
        p1=0
        p2=len(arr)-1

        while(p1<p2):
            #swap the element at p1 and p2
            arr[p1],arr[p2]=arr[p2],arr[p1]
            
            #move the left pointer one step to the right
            p1+=1

            #move the right pointer one step to the left
            p2-=1

sol=Solution()

arr=[1,2,3,4,5]

sol.reverseArray(arr)
print(arr)