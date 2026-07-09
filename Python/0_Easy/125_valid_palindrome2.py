"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

"""


#O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Create to variables to compare
        forward = ""
        backward = ""

        # iterate through each character and check if alphanumeric
        for char in s:
            if char.isalpha() or char.isdigit():
                forward += char.lower()
                backward = char.lower() + backward

        # Check if equal
        if forward == backward:
            return True
        else:
            return False


if __name__ == "__main__":

    solution = Solution()
    test = "0P"
    print(solution.isPalindrome(test))