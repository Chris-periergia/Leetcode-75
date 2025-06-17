

class Solution:
    def countBits(self, n: int) -> List[int]:
        
        arr,count=[],0

        for i in range(0,n+1):

            while i>0:
                count+=i&1
                i>>=1

            arr.append(count)
            count=0
        
        return arr
            
        
        