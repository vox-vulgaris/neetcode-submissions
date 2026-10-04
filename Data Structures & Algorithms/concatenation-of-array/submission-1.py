class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_size = len(nums)
        for i in range(nums_size):
            nums.append(nums[i])
        return nums