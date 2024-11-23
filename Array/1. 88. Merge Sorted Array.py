# Link: https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m-1
        j = n - 1
        k = m + n - 1
        while j > -1:
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        # alternative
        # for i in range(m, m+n):
        #     nums1[i] = nums2[i-m]
        # nums1.sort()


# Self Reflection 
'''
    same as merge sort algorithms merge function 
    but just do it in a backward fashion since we have to 
    do it in space. 
'''
