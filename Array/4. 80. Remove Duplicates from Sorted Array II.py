# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # i = 0
        # l = len(nums)
        # c = 1
        # for j in range(1, l):
        #     if nums[j] == nums[i] and c < 2:
        #         c += 1
        #         i += 1
        #         nums[i] = nums[j]
        #     elif nums[j] != nums[i]:
        #         i += 1
        #         c = 1
        #         nums[i] = nums[j]
        # return i+1

        j = 2
        l = len(nums)
        for i in range(2, l):
            if nums[i] != nums[j-2]:
                nums[j] = nums[i]
                j += 1
        return j





# Self Reflection 

'''
    This problem was quite challanging at first 
    (ii)
    use two pointer i -> 2..n j -> 2 
    if nums[i] != nums[j-2] then nums[j] = nums[i] #from the solution

    (i)
    another way is to use a counter and lock i's position and change it. # I came up with
    # kindda making it complex but it gets the work done. 
'''