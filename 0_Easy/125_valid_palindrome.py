"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise."""

"""
Edge Case = blank string, all non-alphanuermic characters == True
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
    
    # format and prepare string
    ## upper -> lower case
    ## remove non-alphanumeric characters and spaces
    ### Hello, My Name IS -> hellomynameis

        #Turns out this can be solved in two lines of code
        s_formatted = ''.join(char.lower() for char in s if char.isalnum())
       
        # Check if the formatted string is the same as its reverse
        ## use sliding to basically reverse the string 
        return s_formatted == s_formatted[::-1]






    #     s = s.lower()
    #     s_formatted = ""

    #     for i in s:
    #         if i.isalpha():
    #             s_formatted += i
    #         if i.isdigit():
    #             s_formatted += i

    # # Test if empty string
    #     if s_formatted == "":
    #         return True

    # # reverse order of char in string
    #     s_reverse = ""
    #     s_array = list()

    #     for i in s_formatted:
    #         s_array.append(i)

    #     for x in range(len(s_array)-1, -1, -1):
    #         s_reverse += s_array[x]



    # see if reversed string == string 
        # if s_formatted == s_reverse:
        #     return True
        # else: return False

    


    
if __name__ == "__main__":
    solution = Solution()
    test_string = "A man, a plan, a canal: Panama" 
    
    print(solution.isPalindrome(test_string))