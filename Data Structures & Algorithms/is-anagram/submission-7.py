class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        result = {}
        for char in s:
            result[char] = result.get(char, 0) + 1
        for char in t:
            if char not in result or result[char] == 0:
                return False 
            else:
                result[char] -= 1
        return True 