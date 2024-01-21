class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;
        
        long temp = x, rev = 0;

        while (temp) {
            rev = rev*10 + temp%10;
            temp /= 10;
        }

        return x==rev;
    }
};