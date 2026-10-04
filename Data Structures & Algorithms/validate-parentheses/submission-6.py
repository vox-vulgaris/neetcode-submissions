class Solution:
    def isValid(self, s: str) -> bool:
        s_stack = [None]
        opening = ['(', '[', '{']
        closing = [')', ']', '}']
        opening_count = 0
        closing_count = 0
        for i in range(len(s)):
            if s[i] in closing:
                if s_stack[len(s_stack) - 1] != opening[closing.index(s[i])]:
                    return False
                else:
                    closing_count += 1
                    del s_stack[len(s_stack) - 1]
            else:
                opening_count += 1
                s_stack.append(s[i])
        if opening_count == closing_count:
            return True
        else:
            return False 