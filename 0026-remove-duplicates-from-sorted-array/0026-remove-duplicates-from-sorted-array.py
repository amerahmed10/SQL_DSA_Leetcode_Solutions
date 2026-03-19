class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        nums.reverse()
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i],0)
            
        for key,value in count.items():
            if value>1:
                for i in range(0,value-1):
                    nums.remove(key)
        
        nums.reverse()
        return len(nums)


        