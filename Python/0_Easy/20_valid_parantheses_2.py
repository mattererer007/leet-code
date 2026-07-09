from collections import deque

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""


class Solution:
    def isValid(self, input: str) -> bool:

        # Create a stack (LIFO) 
        open_brackets = deque()

        # itearate through each character in string
        for x in input:
            #if open, push to stack tracking open facing brackets
            if x in ['[', '{', '(']:
                open_brackets.append(x)

            # If closed, check if the LIFO open bracket matches it 
            elif len(open_brackets) > 0:
                lifo = deque.pop(open_brackets)

                if lifo == '(' and x != ')':
                    return False
                elif lifo == '{' and x != '}':
                    return False
                elif lifo == '[' and x != ']':
                    return False
            # For situations where there is an outlying closed bracket in the beginning or end of string
            else:
                return False
                
        # Ensure all open brackets have been resolved
        if len(open_brackets) > 0:
            return False
                
        return True




















# Test case
if __name__ == "__main__":
    solution = Solution()
    input_string = '([]{})'

    result = solution.isValid(input_string)
    print (result)
    