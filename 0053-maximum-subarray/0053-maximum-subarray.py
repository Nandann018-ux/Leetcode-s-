class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = nums[0]
        max_s = nums[0]

        for i in range(1,len(nums)):
            cur = max(nums[i],cur + nums[i])
            max_s = max(max_s,cur)
        
        return max_s