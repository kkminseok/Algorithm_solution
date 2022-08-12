**c++**

```c++
class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        unordered_map<int,int> um;
        int maxcol = 0;
        int res = wall.size();
        int height = res;
        for(int i = 0 ;i<height; ++ i){
            int sum = 0;
            for(int j = 0 ; j <wall[i].size();++j){
                sum += wall[i][j];
                um[sum]++;
            }
            maxcol = sum;
        }
        for(auto it = um.begin(); it!=um.end();++it){
            if(it->first == maxcol) continue;
            res = min(res, height- it->second);
        }
        return res;
    }
};

```