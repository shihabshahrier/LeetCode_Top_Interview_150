# Link : https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=1
        l = len(nums)
        while j < l:
            if nums[j] != nums[i]:
                nums[i+1] = nums[j]
                i+=1
                j+=1
            else:
                j+=1   
        return i+1
    
# Self Reflection 

'''
    Quite same as 27
    just use two pointer i -> 1st j -> 2nd 
    if j doesn't hold dublicate just replace it with i+1
'''