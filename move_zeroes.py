def find_nonzero_pointer(list, nonzero_index):
    while(nonzero_index <len(list)):
        if list[nonzero_index] != 0:
            break
        else:
            nonzero_index += 1
    return nonzero_index

def find_zero_pointer(list, zero_index):
    
    while(zero_index <len(list)):
        if list[zero_index] == 0:
            break
        else:
            zero_index += 1
    return zero_index
        
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        nonzero = 0
        zero = 0
        while(True):
            zero = find_zero_pointer(nums, zero)
            nonzero = find_nonzero_pointer(nums, nonzero)
            if zero >= len(nums) or nonzero >= len(nums):
                break
            if nonzero > zero and nonzero != len(nums):
                nums[nonzero], nums[zero] = nums[zero], nums[nonzero]
            else:
                nonzero += 1
                continue
        