class Solution:
    def largestGoodInteger(self, num: str) -> str:
        str_out = '0'

        for idx in range(len(num)-2):
            if num[idx] == num[idx+1] == num[idx+2]:
                str_out = max(str_out, num[idx]*3)
            
        return str_out if str_out != '0' else ""