```c++
class Solution {
public:
    int findLHS(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int result =0;
        int countnumf = 1;
        int countnums = 0;
        int spot = nums[0];
        bool check = false;
        for(size_t i=0;i<nums.size();++i)
        {
            cout<<"i : "<<i<<'\n';
            spot = nums[i];
            while(i+1<nums.size() && spot == nums[i+1])
            {
                ++countnumf;
                ++i;
            }
            spot = nums[i]+1;
            while(i+1<nums.size() && spot ==nums[i+1])
            {
                check = true;
                ++countnums;
                ++i;
            }
            cout<<countnumf<<" "<<countnums<<'\n';
            if(countnums!=0)
                result = max(countnumf + countnums ,result);
            countnumf = countnums == 0 ? 1 : countnums;
            countnums = 0;
            if(check)
            {
                --i;
                check=false;
            }
            
        }
        
        return result;
    }

};
```