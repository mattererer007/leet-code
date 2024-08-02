from collections import Counter
"""
Two strings are considered close if you can attain one from the other using the following operations:

    Operation 1: Swap any two existing characters.
        For example, abcde -> aecdb
    Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
        For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

You can use the operations on either string as many times as necessary.

All lower case, no space or non-letters
"""

# Edge Case: blank string, different lengths, null, 

# To Resolve Option1: order each string and see if they same 


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if word1 is not None and word2 is not None and (len(word1) == len(word2)):
                        
            #Option1
            if (self.stringToList(word1) == self.stringToList(word2)):
                return True

            #Option2a - check that the same letters are present to enable swappinh
            unique_letters1, unique_letters2 = self.uniqueLetters(word1), self.uniqueLetters(word2)

            if len(unique_letters1 - unique_letters2) > 0 or len(unique_letters2 - unique_letters1) > 0:
                return False

          
            #Option2b -- check if the counts of the letters are the same to enable swapping
            count1, count2 = self.letterCount(word1), self.letterCount(word2)

            for i in range(len(count1)):
                if count1[i] - count2[i] != 0:
                    return False
            
            return True

        return False
    
    def  stringToList(self, input):
        word_list = []
        for x in input:
            word_list.append(x)

        word_list.sort()   

        return word_list
    
    def uniqueLetters(self, input):
        unique_letters = set(self.stringToList(input))
        return unique_letters

    def letterCount(self, input):
        track_count = {}
        for x in input:
            if x in track_count:
                track_count[x] += 1
            else: track_count[x] = 1

        count_list = []
        for val in track_count.values():
            count_list.append(val)
            count_list.sort()

        return count_list 
            
    def closeStrings2(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        c1=Counter(word1)
        c2=Counter(word2)

        if set(c1.keys())!=set(c2.keys()):
            return False
        if sorted(c1.values()) != sorted(c2.values()):
            return False
        return True
            


if __name__ == '__main__':

    solution = Solution()
   
    word1 = "hello"
    word2 = "hhelo"

    print(solution.closeStrings2(word1, word2))
