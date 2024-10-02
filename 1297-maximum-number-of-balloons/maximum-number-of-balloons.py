class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letter_count = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        double_letters = ['l', 'o']

        for char in text:
            if char not in letter_count:
                continue
            letter_count[char] += 1
        
        minimum = min(letter_count, key=lambda x: letter_count[x])

        if minimum in double_letters:
            return letter_count[minimum] // 2
        
        if letter_count['l'] >= 2*letter_count[minimum] \
        and letter_count['o'] >= 2*letter_count[minimum]:
            return letter_count[minimum]
        
        lo_min = min(letter_count['l'], letter_count['o'])
        return lo_min // 2
        
