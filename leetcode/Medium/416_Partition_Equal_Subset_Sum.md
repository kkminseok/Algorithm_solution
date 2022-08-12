**c++**

```c++
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = 0;
        for(int num : nums)
            sum+=num;
        if(sum%2) return false;
        
        sum/=2;
        
        int n = nums.size();
        bool** p = new bool*[n+1];
        for(int i = 0 ; i < n+1;++i)
            p[i] = new bool[sum+1];
        
        for(int i = 0;i<n+1;++i){
            for(int j = 0 ; j <sum+1;++j)
                p[i][j] = false;
        }
        p[0][0] = true;
        
        for(int i = 1; i<n+1;++i)
            p[i][0] = true;
        for(int j =1 ; j<sum+1;++j)
            p[0][j] = false;
        
        for(int i =1 ; i<n+1;++i){
            for(int j = 1 ; j<sum+1;++j){
                p[i][j] = p[i-1][j];
                if(j>= nums[i-1])
                    p[i][j] = (p[i][j] || p[i-1][j - nums[i-1]]);
                cout<<p[i][j]<<" ";
            }
            cout<<'\n';
        }
        
        
        return p[n][sum];
    }
};



```