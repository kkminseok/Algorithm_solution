```c++
bool pred(pair<int,int> a,pair<int,int> b)
{
    if(a.second==b.second)
        return a.first<b.first;
    return a.second < b.second;
}

class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        vector<int> result;
        vector<pair<int,int>> vec;
        for(size_t i = 0;i<mat.size();++i)
        {
            int sum = 0;
            for(size_t j =0;j<mat[i].size();++j)
            {
                if(mat[i][j]==1)
                    ++sum;
            }
            vec.push_back(make_pair(i,sum));
        }
        sort(vec.begin(),vec.end(),pred);
        
        for(int i=0;i<k;++i)
        {
            result.push_back(vec[i].first);
        }
        
        return result;
    }
};
```