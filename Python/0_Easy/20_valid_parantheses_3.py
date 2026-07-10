from collections import deque

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        opener = {'(', '[', '{'}
        closer = {')': '(', ']': '[', '}': '{'}

        fifo = deque()

        count = 0
        for character in s:
            if character in opener:
                fifo.append(character)
                count+=1
            else:
                try:
                    check = fifo.pop()
                    if check != closer[character]:
                        return False
                    else:
                        count -=1
                except:
                    return False
        

        if count > 0: 
            return False
        else: 
            return True
            


        




if __name__ == "__main__":
    solution = Solution()
    input_string = '()[]}'

    result = solution.isValid(input_string)
    print (result)
    