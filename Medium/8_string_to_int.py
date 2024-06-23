"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

    Whitespace: Ignore any leading whitespace (" ").
    Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
    Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
    Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.

Return the integer as the final result.
"""

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        number = ""
        sign = 1
        valid_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        # Strip string of white space and convert into a list of characters
        s = s.strip()  # remove leading and trailing whitespace
        if not s:
            return 0

        s_list = list(s)

        if s_list[0] == "-":
            sign = -1
            s_list[0] = '0'
        elif s_list[0] == "+":
            s_list[0] = '0'


        for n in s_list:
            if n in valid_numbers:
                number += n
            else:
                break

        if number == "":
            return 0
        
        return_number = sign * int(number)

        if return_number > 2**31 - 1:
            return 2**31 - 1
        elif return_number < -2**31:
            return -2**31
        else: return return_number



if __name__ == "__main__":
    solution = Solution()
    test_result = "" 
    print(solution.myAtoi(test_result))

