class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = {char: 0 for char in "balloon"}

        for char in text:
            if char not in letters:
                continue
            letters[char] += 1

        letters['l'] //= 2
        letters['o'] //= 2

        minimum = min(letters, key=lambda x: letters[x])

        return letters[minimum]
