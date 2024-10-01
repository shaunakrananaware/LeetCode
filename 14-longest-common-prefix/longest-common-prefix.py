class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest_size = len(strs[0])
        smallest_word = strs[0]
        prefix = ""

        for i in strs:
            if len(i) < smallest_size:
                smallest_size = len(i)
                smallest_word = i

        if not smallest_size:
            return ''

        checking = True

        for i in range(smallest_size):
            for j in strs:
                if j[i] != smallest_word[i]:
                    checking = False
                    break
            
            if checking:
                prefix += smallest_word[i]
            else:
                return prefix
            
        return prefix