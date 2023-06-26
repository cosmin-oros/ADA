# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
# valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    def isValid(self, s):
        stack = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            # check if it's a closing parentheses
            if c in closeToOpen:
                # check if they match
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                # if we get an opening parentheses
                stack.append(c)
        # if the stack is empty then it's valid
        return True if not stack else False


sol = Solution()
s = "()[]{}"
print(sol.isValid(s))