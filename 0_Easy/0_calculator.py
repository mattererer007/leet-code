from typing import List

"""
Build a calculator. Assume no errors

"""
 #O(n) time complexity as list is iterated through only once by two disconnected loops
class Solution:
    def calculator(self, function: List) -> int:

        mult_div_list = []
        pointer = -1

        i = 0
        while i < len(function):
            if function[i] == 'x':
                mult_div_list[pointer] = mult_div_list[pointer] * function[i+1]
                i += 2

            elif function[i] == '/':
                mult_div_list[pointer] = mult_div_list[pointer] // function[i+1]
                i+=2
            else:
                mult_div_list.append(function[i])
                i+=1
                pointer += 1
            
            print(mult_div_list)

        if len(mult_div_list) == 1:
            return mult_div_list[0]
        
        total = mult_div_list[0]
        for i in range(0, len(mult_div_list)):
            if mult_div_list[i] == '+':
                total += mult_div_list[i+1]
            elif mult_div_list[i] == '-':
                total -= mult_div_list[i+1]

        return total

if __name__ == "__main__":

    function = [1, 'x', 2, 'x', 4, 'x', 6, '/', 2]
    
    solution = Solution()
    print(solution.calculator(function))