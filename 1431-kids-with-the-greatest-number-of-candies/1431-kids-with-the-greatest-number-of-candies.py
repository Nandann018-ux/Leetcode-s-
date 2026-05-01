class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxx = max(candies)
        ans = []

        for candies in candies:
            if candies + extraCandies >= maxx:
                ans.append(True)
            else:
                ans.append(False)

        return ans
        