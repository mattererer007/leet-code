"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
        reverse_new_string = ""

        for i in s:
            if i != " " and i.isalnum():
                new_string += i.lower()
                reverse_new_string = i.lower() + reverse_new_string

        return new_string == reverse_new_string

if __name__ == "__main__":
    solution = Solution()
    test_string = "A man, a plan, a canal: Panama" 
    
    print(solution.isPalindrome(test_string))