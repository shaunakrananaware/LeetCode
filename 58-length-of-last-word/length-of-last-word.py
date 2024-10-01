class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        currentLength = 0
        spaceStatus = False
        
        for i in s:
            if i == ' ':
                spaceStatus = True
                continue
            if spaceStatus == True:
                spaceStatus = False
                currentLength = 0

            currentLength += 1
        
        return currentLength