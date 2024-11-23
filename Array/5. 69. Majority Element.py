
# Link: https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]

  
    
# Self Reflection 

'''
    # Easy but there is a catch
    if we sort the array then the majority element will definitely 
    appear in the middle.
''' 