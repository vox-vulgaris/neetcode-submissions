class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # two pointers:
        # right pointer: traverse array, detect when current value is unique
        # detection: prior value not equal to right pointer's present value
        # left pointer: at position following most recent unique value
        # increment left pointer by one each time there's a detection of unique value
        l = 1
        for r in range(1, len(nums)):
            if nums[r - 1] != nums[r]:
                nums[l] = nums[r]
                l += 1
        return l