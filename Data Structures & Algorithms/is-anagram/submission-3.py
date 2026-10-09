class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = {}
        for char in s:
            if char not in result.keys():
                result[char] = 1
            else:
                result[char] += 1
        for char in t:
            if char not in result.keys():
                result[char] = -1
            else:
                result[char] -= 1        
        if len(s) != len(t):
            return False
        else:
            if (set(result.values()) != {0}):
                return False
            else:
                return True 
