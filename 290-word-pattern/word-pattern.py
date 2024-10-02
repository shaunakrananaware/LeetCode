class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sentence_arr = s.split(' ')

        if len(pattern) != len(sentence_arr): return False

        pattern_dict = {}

        for idx in range(len(pattern)):
            if pattern[idx] not in pattern_dict:
                if sentence_arr[idx] in pattern_dict.values():
                    return False 
                pattern_dict[pattern[idx]] = sentence_arr[idx]
                continue
            if pattern_dict[pattern[idx]] != sentence_arr[idx]:
                return False


        return True