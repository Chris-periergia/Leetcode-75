
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        curr_sum=sum(nums[:k])
        windows_sum=curr_sum
    

        for i in range(len(nums)-k):
            curr_sum+=nums[i+k]-nums[i]
            windows_sum=max(curr_sum,windows_sum)
        
        return windows_sum/k
        