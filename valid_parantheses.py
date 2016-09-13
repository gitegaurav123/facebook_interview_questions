class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char in ['{', '(','[']:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                open_bracket = stack.pop()
                if open_bracket == '(' and char == ')':
                    continue
                elif open_bracket == '[' and char == ']':
                    continue
                elif open_bracket == '{' and char == '}':
                    continue
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False