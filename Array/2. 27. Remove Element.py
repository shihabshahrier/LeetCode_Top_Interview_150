# link : https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = len(nums) - 1
        i = 0
        while i <= j:
            if nums[i] == val and nums[j] != val:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
                j -= 1
            elif nums[j] == val:
                j -= 1
            else:
                i += 1
        return j+1
    
# Self Reflection 

'''
    Quite simple 
    just use two pointer i -> first j -> last 
    relocate if val found in i and j is not val
'''