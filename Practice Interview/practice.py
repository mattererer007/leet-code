"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

    "{" == invalid
    "([])" = valid 

    ([)]

    True (valid) or False

    (hello[world])

    O(n)
 """

"""Proposed Solution"""

# intake a string

#iterate through each char in string

# if string is None: return false
# if string starts with close brack } ] ) and there is no open brack then return false 
# if open bracket add to queue and then next clsoe bracket should match latest open bracket, if so >> pop that open bracket and continue through list


# ([])  queue  [ (  >> ]

class Solution(object):
    def valid_paranth(self, s: str) -> bool: 

        open_bracket = "([{"
        tracker = []

        if s is None:
            return False
        
        for c in s:
            if c not in open_bracket and len(tracker) < 1: # check for closing braket with no possible opening bracket
                return False
            elif c in open_bracket: # check if opening bracket
                tracker.append(c)

            else:
                if c == ')' and tracker.pop() == '(':
                    continue
                elif c == '}' and tracker.pop() == '{':
                    continue
                elif c == ']' and tracker.pop() == '[':
                    continue
                else:
                    return False
                
        if len(tracker) > 0:
            return False
        else:
            return True
    
if __name__ == "__main__":
    solution = Solution()

    test_string = "]"

    print(solution.valid_paranth(test_string))




        