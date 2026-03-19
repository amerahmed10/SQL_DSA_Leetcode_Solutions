class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        miss = len(nums)
        for i,num in enumerate(nums):
            miss ^= i^num
        return miss
        