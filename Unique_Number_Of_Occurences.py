from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur=defaultdict(int)

        for num in arr:
            occur[num]+=1
        occur=list(occur.values())

        return len(occur)==len(set(occur))
        