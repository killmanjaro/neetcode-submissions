class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] in "({[":
                stack.append(s[i])
                print("stack after appending", stack)
            elif len(stack) == 0:
                return False
            elif s[i] == ")":
                print("stack )", stack)
                elem = stack.pop()
                print("popped", elem)
                print("stack after popping )", stack)
                if elem not in "(":
                    return False
            elif s[i] ==  "}":
                print("stack }", stack)
                elem = stack.pop()
                print("popped", elem)
                print("stack after popping )", stack)
                if elem not in "{":
                    return False
            elif s[i] == "]":
                print("stack ]", stack)

                elem = stack.pop()
                print("popped", elem)
                print("stack after popping )", stack)
                if elem not in "[":
                    return False
            
        if len(stack) == 0:
            return True
        return False
        