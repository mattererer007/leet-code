"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest

that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.
"""

# easy palindrome = duplicate letters (i.e. anything that is even can go into a palindrome)
## Once all even letters are pulled in, then pull in 1 odd option (1,3, 5, etc.) >> will need to be in middle but still possible
### Does not need to be a real word

class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        # sum up all letters that have an even count
        sum_of_even_letters = 0

        # track each unique letter in string and count
        s_hash = {}

        # track the count of the greatest odd numbered letter
        max_odd_letter = 0

        # Other odd letters
        ## For everything else, an odd can become an even if you remove one...so just do that for all the small odd input1
        sum_of_smaller_odd_numbers = 0

        # 1 character present
        char_with_1_entry_present = False
        
        # Iterate through entire string
        for char in s:
            if char in s_hash:
                s_hash[char] += 1
            else:
                s_hash[char] = 1

        # Check if even or odd
        for char in s_hash:

            if s_hash[char] == 1:
                char_with_1_entry_present = True

            if s_hash[char] % 2 == 0:
                sum_of_even_letters += s_hash[char]
            elif s_hash[char] > max_odd_letter:
                # Only add to sum of smaller odd numbers once something has already been added so that we don't go to -1
                if max_odd_letter != 0:
                    sum_of_smaller_odd_numbers += max_odd_letter - 1
                max_odd_letter = s_hash[char]
            else:  # for situations where odd but smaller that current max
                sum_of_smaller_odd_numbers += s_hash[char] - 1  


        # Return
        total = sum_of_even_letters + max_odd_letter + sum_of_smaller_odd_numbers

        if total % 2 == 0 and char_with_1_entry_present == True:
            return total + 1
        else:
            return total

    


if __name__ == "__main__":
    sample = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    sample2 = "ccc"

    solution = Solution()

    print(solution.longestPalindrome(sample2))
