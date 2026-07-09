from typing import List

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

class TrieNode:
    def __init__(self, letter = None):
        self.letter = letter
        self.children = {} # list of all letters directly connected to given node (at beginning will be a null root node)
        self.end_of_word = False # check if current node is the end of a given list of letters (i.e., end of word)


class Solution:

    # O(n) where n is the number of characters found in the list of words provided
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # Create Trie Data Structure
        root = TrieNode()

        # string to capture levels of Trie that have only 1 child
        longest_prefix = ""

        # add each word in string to Trie 
        for word in strs:
            root = self.insertWord(root, word)

        # create pointer to iterate through Trie
        current_node = root

        # While the current node is not the end of the tree (None)
        # While the current node is not the end of a word (end_of_word Boolean)
        # While all strings inputted contain the given character at the given level of the Trie
        while current_node is not None and current_node.end_of_word is False and len(current_node.children) == 1:

            # clumsy loop to iterate to the 1 value in set
            for index, char in enumerate(current_node.children):
                longest_prefix += current_node.children[char].letter # grab letter from each level
                current_node = current_node.children[char] # grab the next layer of Trie


        return longest_prefix
    
    # O(n) where is is the length of the word being added
    def insertWord(self, root: TrieNode, input: str) -> TrieNode:

        # Create pointer to iterate from root through word adding letters at each level of tree if letter not already present
        current_node = root

        for char in input:
            if char in current_node.children:  # if letter already in a level, then continue (means prefix is same so far)
                current_node = current_node.children[char]
            else:  # If letter not at a current level, then add letter as a child of current node and continue
                current_node.children[char] = TrieNode(letter=char)
                current_node = current_node.children[char]
        
        # Once out of letters, the current letter should be tagged as end of word to denot that input to Trie is complete
        current_node.end_of_word = True

        return root
    
if __name__ == "__main__":
    strs = ["dog","doggie","doge"]

    solution = Solution()
    print(solution.longestCommonPrefix(strs))

