class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if ( nums.size() == 0 ) return 0;
        if ( nums.size() == 1 ) return 1;

        int cmp = nums[0];

        for ( auto itr = nums.begin()+1 ; itr < nums.end() ; ) {
            if ( *itr == cmp ) nums.erase(itr);
            else cmp = *itr++;
        }

        return nums.size();
    }
};