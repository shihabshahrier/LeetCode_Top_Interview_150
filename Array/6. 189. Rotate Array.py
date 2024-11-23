# Link: https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        l = len(nums)
        if k > 0:
            nums[:k], nums[k:] = nums[l-k:], nums[:l-k] 

# Self Reflection 

'''
    # Easy 
    first kth <-> Kth to last
    
''' 
