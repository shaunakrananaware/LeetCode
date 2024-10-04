class Solution:
    def largestGoodInteger(self, num: str) -> str:
        num_freq = Counter(num)
        min_3_freq = [key for key, value in num_freq.items() if value >= 3]

        min_3_freq.sort(reverse=True)

        for i in min_3_freq:
            if i*3 in num:
                return i*3
        return ""