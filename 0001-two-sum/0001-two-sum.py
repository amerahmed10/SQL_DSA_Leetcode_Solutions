class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            left = target-nums[i]
            dict[left] = i
        
        for i in range(len(nums)):
            if nums[i] in dict and i!=dict.get(nums[i]):
                return [i,dict.get(nums[i])]
        
        
        