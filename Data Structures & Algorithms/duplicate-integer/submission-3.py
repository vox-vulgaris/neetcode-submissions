class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        len_nums = len(nums)
        len_set_nums = len(set_nums)
        if (len_nums > len_set_nums):
            return True
        else:
            return False