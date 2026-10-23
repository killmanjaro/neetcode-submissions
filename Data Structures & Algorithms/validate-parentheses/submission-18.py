class Solution:
    def isValid(self, s: str) -> bool:
        # first attempt
        '''
        stack = []
        for i in range(len(s)):
            if s[i] in "({[":
                stack.append(s[i])
            elif len(stack) == 0:
                return False
            elif s[i] == ")":
                elem = stack.pop()
                if elem not in "(":
                    return False
            elif s[i] ==  "}":
                elem = stack.pop()
                if elem not in "{":
                    return False
            elif s[i] == "]":
                elem = stack.pop()
                if elem not in "[":
                    return False
            
        if len(stack) == 0:
            return True
        return False
        '''

        # using hash
        stack = []
        closeToOpen = {")" : "(", "]": "[", "}": "{" }

        for c in s:
            # if it is a closing parenthesis
            if c in closeToOpen:
                # stack[-1] is last val in stack
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        return False


