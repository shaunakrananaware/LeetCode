class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_freq = Counter(chars)
        output = 0

        for word in words:
            char_freq = Counter(word)
            current_output = 0
            for key, value in char_freq.items():
                if key not in chars_freq or char_freq[key] > chars_freq[key]:
                    current_output = 0
                    break
                current_output += char_freq[key]
            
            output += current_output
        
        return output
                    