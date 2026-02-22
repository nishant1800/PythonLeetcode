# 80. Remove Duplicates from Sorted Array II

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        count = 1
        for i in range(2, len(nums)):
            if nums[i] != nums[count-1]:
                count += 1
                nums[count] = nums[i]

        return count+1