class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myMap = {}
        for num in nums:
            if num in myMap.keys():
                return True
            else:
                myMap[num] = 1
        return False 
