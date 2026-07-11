"""
PRACTICE TASK: PREFIX TREE (TRIE) FOR NLP TOKENIZATION
------------------------------------------------------
Tries are highly optimized trees for prefix matching, crucial for building NLP 
vocabularies, subword tokenizers (like Byte-Pair Encoding or WordPiece dictionaries), 
and auto-complete query systems.

Implementations to write:
1. TrieNode: Structure with child dictionary and `is_end_of_word` boolean flag.
2. Trie.insert(word): Inserts a string word into the Trie.
3. Trie.search(word): Returns True if the word is exactly in the Trie, False otherwise.
4. Trie.starts_with(prefix): Returns True if there is any word starting with the prefix.
5. Trie.tokenize(text): A custom NLP tokenizer helper that segments a string of text 
   into longest matching vocabulary words present in the Trie. Unmatched characters 
   are treated as single tokens.
"""

from typing import List, Dict

class TrieNode:
    def __init__(self):
        # A dictionary mapping characters to TrieNodes
        self.children: Dict[str, 'TrieNode'] = {}
        self.is_end_of_word: bool = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        
        Time Complexity: O(L) where L is length of the word.
        Space Complexity: O(L) in the worst case (all new characters).
        """
        # TODO: Implement this function
        pass

    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the trie.
        
        Time Complexity: O(L)
        Space Complexity: O(1)
        """
        # TODO: Implement this function
        pass

    def starts_with(self, prefix: str) -> bool:
        """
        Returns True if there is any word in the trie that starts with prefix.
        
        Time Complexity: O(P) where P is length of the prefix.
        Space Complexity: O(1)
        """
        # TODO: Implement this function
        pass

    def tokenize(self, text: str) -> List[str]:
        """
        Tokenizes the input text into a list of strings by matching the longest 
        possible words from the Trie dictionary (greedy forward maximum matching).
        If no matches are found at a given position, emit the single character 
        as a token and advance.
        
        Example:
          Trie contains: ["tik", "tok", "tiktok", "shop"]
          text = "tiktokshopgame"
          returns: ["tiktok", "shop", "g", "a", "m", "e"]
          
        Time Complexity target: O(N^2) worst case (or optimized O(N)), where N is length of text.
        Space Complexity target: O(N) for storing tokens.
        """
        # TODO: Implement this function
        pass


# --- Verification Tests ---
if __name__ == "__main__":
    trie = Trie()
    
    print("Testing Insert, Search, StartsWith...")
    trie.insert("tiktok")
    trie.insert("tik")
    trie.insert("shop")
    
    assert trie.search("tiktok") == True
    assert trie.search("tik") == True
    assert trie.search("tok") == False
    assert trie.starts_with("tik") == True
    assert trie.starts_with("to") == False
    print("Trie core functions passed!")

    print("Testing NLP Greedy Tokenization...")
    tokens = trie.tokenize("tiktokshopgame")
    expected = ["tiktok", "shop", "g", "a", "m", "e"]
    assert tokens == expected, f"Expected {expected}, got {tokens}"
    print("Greedy tokenization passed!")
    
    print("\nAll Trie verification tests passed (once you implement them)!")
