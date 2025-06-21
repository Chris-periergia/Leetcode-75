
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        altitude,sum=[0],0

        for i in gain:
            sum+=i
            altitude.append(sum)

        return max(altitude)

        