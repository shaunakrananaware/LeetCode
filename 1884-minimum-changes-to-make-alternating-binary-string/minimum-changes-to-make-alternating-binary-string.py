class Solution:
    def minOperations(self, s: str) -> int:
        # every string should start with 0
        count = 0

        for idx in range(len(s)):
            if idx % 2 and s[idx] == '0': count += 1
            elif not idx % 2 and s[idx] == '1': count += 1

        return count if count <= len(s) // 2 else len(s)-count 