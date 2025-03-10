"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # Check if enough values to create valid string
        if len(s) == 1:
            return False

        # Convert the provided string into a list of characters assume O(n) 
        # with n being the number of characters in string?
        split_s = list(s)

        # Intitiate empty list to hold characters
        s_stack = []

        # Iterate through the list of characters
        for i in range(0, len(split_s)):
            # In instances where the value is an open bracket, add to stack (LAST IN, FIRST OUT)
            if split_s[i] in ['(', '[', '{']:
                s_stack.append(split_s[i])
            # Else if the stack already has items but a non-open bracket is submitted, check 
            # if the item is a closed bracket and whether it correctly closes out an open bracket
            elif len(s_stack) > 0:
                if split_s[i] == ')':
                    if s_stack.pop() == '(':
                        continue
                    else: return False

                if split_s[i] == ']':
                    if s_stack.pop() == '[':
                        continue
                    else: return False

                if split_s[i] == '}':
                    if s_stack.pop() == '{':
                        continue
                    else: return False
            else: return False
        
        # Check if there are open brackets that are still open 
        if len(s_stack) > 0:
            return False
        else: return True
    

# Test case
if __name__ == "__main__":
    solution = Solution()
    input_string = '{}'

    result = solution.isValid(input_string)
    print (result)
    
