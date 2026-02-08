class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        max_water = 0

        while l < r:
            h = min(height[l], height[r])
            w = r - l
            area = h * w
            max_water = max(max_water, area)


            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_water
        