class Solution:
    def firstUniqChar(self, s: str) -> int:
        letter_idx = {}
        repeating = set()

        for idx, char in enumerate(s):
            if char not in letter_idx: 
                letter_idx[char] = idx
                continue
            repeating.add(char)
        
        for i in repeating: letter_idx[i] = 10**5 

        min_idx_char = min(letter_idx, key=lambda x: letter_idx[x])

        return letter_idx[min_idx_char] if letter_idx[min_idx_char] != 10**5 else -1
