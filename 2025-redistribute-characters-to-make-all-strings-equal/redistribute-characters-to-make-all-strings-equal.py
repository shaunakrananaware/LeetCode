class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        letter_freq = defaultdict(int)
        for word in words:
            for letter in word:
                letter_freq[letter] += 1
        
        for i in letter_freq.values():
            if i % len(words): return False
        
        return True