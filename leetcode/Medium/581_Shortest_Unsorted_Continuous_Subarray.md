```c++
class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        vector<int> temp = nums;
        sort(temp.begin(),temp.end());
        int left = 0;
        int right= nums.size()-1;
        while(left<nums.size() && nums[left]==temp[left])
            ++left;
        if(left==nums.size())
            return 0;
        while(right>=0 &&nums[right]==temp[right])
            --right;
        return right-left+1;
    }
};
```