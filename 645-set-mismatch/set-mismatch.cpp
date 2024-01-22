class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int missing, repeat;
        unordered_map <int, int> mp;

        for ( int i=1 ; i <= nums.size() ; i++) mp[i]++;
        for ( int i : nums ) mp[i]--;

        for ( auto a : mp ) {
            if ( a.second == -1 ) repeat = a.first;
            if ( a.second == 1 ) missing = a.first;
        }

        return { repeat, missing };
    }
};