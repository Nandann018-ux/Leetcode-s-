class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pre = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in pre:
                return [pre[diff],i]
            pre[n] = i