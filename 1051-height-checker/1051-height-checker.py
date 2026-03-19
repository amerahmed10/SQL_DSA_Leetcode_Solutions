class Solution(object):
    def countingSort(self,arr):
        count={}
        for i in range(len(arr)):
            count[arr[i]]= 1+count.get(arr[i],0)
        
        min_v,max_v=min(arr),max(arr)

        index=0

        for i in range(min_v,max_v+1):
            while count.get(i,0)>0:
                arr[index]=i
                count[i] = count[i]-1
                index += 1
        
        return arr
    
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        count=0
        sorted_heights = heights[:]
        sorted_heights = self.countingSort(sorted_heights)
        for i in range(len(sorted_heights)):
            if sorted_heights[i]!=heights[i]:
                count += 1
        return count
        