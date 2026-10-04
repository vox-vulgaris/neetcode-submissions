class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # two pointers:
        # right pointer: traverse array, detect when current value is unique
        # detection: prior value not equal to right pointer's present value
        # left pointer: at position following most recent unique value
        # increment left pointer by one each time there's a detection of unique value
        i = 1
        for j in range(1, len(nums)):
            if nums[j - 1] != nums[j]:
                nums[i] = nums[j]
                i += 1
        return i