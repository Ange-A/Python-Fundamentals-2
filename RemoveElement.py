##Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

##

class Solution(object):
    def removeElement(self, nums, val):

        s = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[s] = nums[i]
                s +=1
        return s
