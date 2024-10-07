class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for idx in range(len(haystack)):
            if haystack[idx] != needle[0] or len(haystack)-idx < len(needle):
                continue
            
            match = True
            for jdx in range(1, len(needle)):
                if needle[jdx] == haystack[idx+jdx]:
                    continue
                match = False
                break
            
            if match: return idx
        
        return -1


