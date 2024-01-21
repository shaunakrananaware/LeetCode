class Solution {
public:
    bool check(vector<int>& nums) {
        int acsndBreaks = 0;

        for ( int i=1 ; i<nums.size() ; i++ ) 
            if ( nums[i] < nums[i-1] ) acsndBreaks++;
        
        if ( acsndBreaks != 0 &&
            nums[ nums.size()-1 ] > nums[0] ) acsndBreaks++;

        if (acsndBreaks > 1) return false;
        else return true;
    }
};