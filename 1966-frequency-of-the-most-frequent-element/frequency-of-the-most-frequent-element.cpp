class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());

        long ans = 1, low = 0, high = 0, sum = 0, diff, windowSize;

        while(high < nums.size()) {
            sum += nums[high];
            windowSize = high - low + 1;
            diff = windowSize * nums[high] - sum;

            while (diff > k && low < high) {
                sum -= nums[low];
                diff -= nums[low];
                windowSize--; low++;
            }

            ans = max(ans, windowSize);

            high++;
        }

        return ans;
    }
};