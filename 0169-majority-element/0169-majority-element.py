class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter=1
        curr=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==curr:
                counter += 1
            else:
                counter -= 1
            if counter==0:
                curr=nums[i]
                counter=1
        return curr
        