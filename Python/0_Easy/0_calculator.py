from typing import List

"""
Build a calculator. Assume no errors

"""
#O(n) time complexity as list is iterated through only once by two disconnected loops
## Solution assumes that there will be no incorrect mathematical statements given (i.e, / 0)
## Solution first will iterate through the mathematical priorities of functions start with multiple and divide 
## Before moving to addition and subtraction
class Solution:
    def calculator(self, function: List) -> int:


        stack = []
        i = 0

        # iterate through list of numbers and strings provided
        while i < len(function):
            token = function[i]
            # If a multiplier or divider comes up...
            ## Pull the last number added and perform function witht he next number
            if token == 'x' or token == '/':
                previous_input = stack.pop()
                next_input = function[i+1]
                if token == 'x':
                    stack.append(previous_input * next_input)
                else:
                    stack.append(previous_input // next_input)
                
                i += 2 # Skip 2 ahead so as not to re-review the next_input
            else: # Add everything else to the list
                stack.append(token)
                i += 1

        # Result starts as the first number in the stack
        result = stack[0]
        # Skip 1 ahead and iterate through remaining addition and subtraction functions
        i = 1
        while i < len(stack):
            operator = stack[i]
            next_number = stack[i+1]
            if operator == '+':
                result += next_number
            elif operator == '-':
                result -= next_number
            
            i += 2

        return result
    


if __name__ == "__main__":

    function = [1, 'x', 2, 'x', 4, 'x', 6, '/', 2]
    
    solution = Solution()
    print(solution.calculator(function))