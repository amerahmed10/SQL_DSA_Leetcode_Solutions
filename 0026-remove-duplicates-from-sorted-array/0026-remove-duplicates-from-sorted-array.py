class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 1
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:
                nums[index]=nums[i]
                index += 1
        return index
            



        