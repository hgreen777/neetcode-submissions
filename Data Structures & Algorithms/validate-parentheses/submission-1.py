class Solution:
    def isValid(self, s: str) -> bool:
        di = {'[':']', '{':'}', '(':')'}
        stack = []
        for c in s:
            if c in di.keys():
                stack.append(c)
            elif c in di.values():
                if len(stack) == 0:
                    return False
                if di[stack.pop()] != c:
                    return False

        if len(stack) == 0:
            return True
        return False