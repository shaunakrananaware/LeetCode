class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        letter_idx = {}
        max_length = -1

        for idx, char in enumerate(s):
            if char not in letter_idx:
                letter_idx[char] = idx
                continue
            max_length = max(max_length, idx-letter_idx[char]-1)

        return max_length