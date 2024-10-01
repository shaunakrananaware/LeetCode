class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_letters = {}

        for idx in range(len(s)):
            if s[idx] not in s_letters:
                if t[idx] in s_letters.values():
                    return False
                s_letters[s[idx]] = t[idx]
                continue
            
            if s_letters[s[idx]] != t[idx]:
                return False
            
        return True
            
