class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        my_set = set()
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                my_set.add(nums1[i])
        my_list = list(my_set)
        return my_list
        