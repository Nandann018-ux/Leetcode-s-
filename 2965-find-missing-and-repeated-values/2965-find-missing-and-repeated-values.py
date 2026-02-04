class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        seen = set()
        repeat = -1
        actual_sum = 0
        
        for row in grid:
            for num in row:
                actual_sum += num
                if num in seen:
                    repeat = num
                else:
                    seen.add(num)
        
        total = n * n
        expected_sum = total * (total + 1) // 2
        missing = expected_sum - (actual_sum - repeat)
        
        return [repeat, missing]