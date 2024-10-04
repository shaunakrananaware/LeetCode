class Solution:
    def maxScore(self, s: str) -> int:
        l_score = 0 if int(s[0]) else 1
        r_score = 0
        for idx in range(1, len(s)):
            if s[idx] == '1': r_score += 1
        max_score = l_score + r_score

        for idx in range(1, len(s)-1):
            if s[idx] == '0': l_score += 1
            else: r_score -= 1
            max_score = max(max_score, l_score+r_score)
        
        return max_score