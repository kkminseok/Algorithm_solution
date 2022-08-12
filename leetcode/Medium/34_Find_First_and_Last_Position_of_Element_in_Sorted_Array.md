```c++
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int start = 0;
        int end=nums.size()-1;

        vector<int> result;
        while(start<=end)
        {
            int mid = (start+end)/2;
            cout<<start<<" "<<mid<<" "<<end<<'\n';
            if(target==nums[mid])
            {
                start = mid;
                end = mid;
                while(start-1 >=0 && nums[start-1] ==target)
                    start--;
                while(end+1 <nums.size() && nums[end+1] == target)
                    ++end;
                result.push_back(start);
                result.push_back(end);
                return result;
            }
            else if(target>nums[mid])
            {
                start = mid+1;
            }
            else
                end=mid-1;
        }
        result.push_back(-1);
        result.push_back(-1);
            
        return result;
    }
};
```