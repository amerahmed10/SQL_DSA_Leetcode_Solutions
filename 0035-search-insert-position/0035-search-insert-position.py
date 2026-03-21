class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left,right=0,len(nums)-1

        if nums[0]>target:
            return 0
        
        elif nums[-1]<target:
            return len(nums)
    
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left = mid+1
            elif nums[mid]>target and nums[mid-1]<target:
                return mid
            else:
               right= mid-1