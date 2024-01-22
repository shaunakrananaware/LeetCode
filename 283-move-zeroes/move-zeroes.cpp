class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int zeroCount = 0;
        vector<int>::iterator itr = nums.begin();

        for ( ; itr < nums.end() - zeroCount ; ) {
            if ( *itr == 0 ) {
                nums.erase(itr);
                nums.push_back(0);
                zeroCount++;
            } else itr++;
        }
    }
};