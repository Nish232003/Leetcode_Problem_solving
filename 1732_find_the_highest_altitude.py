class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        curr = 0
        for i in gain:
            curr += i
            ans = max(ans , curr)
        return ans
