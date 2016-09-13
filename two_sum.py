class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        
        for index, number in enumerate(nums):
            if number in dict:
                return dict[number], index
            else:
                dict[target-number] = index
        
        return None, None
                