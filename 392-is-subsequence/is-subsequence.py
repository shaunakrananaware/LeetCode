class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not len(s):
            return True
        if len(s) > len(t):
            return False

        current_matches = 0

        for i in range(len(t)):
            if current_matches < len(s):
                if s[current_matches] == t[i]:
                    current_matches += 1

        return current_matches == len(s)