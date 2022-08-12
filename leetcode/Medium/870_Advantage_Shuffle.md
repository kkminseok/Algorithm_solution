**c++**

```c++
bool pred(pair<int,int>& a,pair<int,int>& b)
{
    if(a.first==b.first)
        return a.second<b.second;
    return a.first<b.first;
}
class Solution {
public:
    vector<int> advantageCount(vector<int>& A, vector<int>& B) {
        vector<pair<int,int>> tempB;
        queue<int> q;
        vector<int> result(A.size());
        for(size_t i =0;i<B.size();++i)
            tempB.push_back(make_pair(B[i],i));
        sort(tempB.begin(),tempB.end(),pred);
        sort(A.begin(),A.end());
        int j = 0;
        for(size_t i = 0;i<A.size();++i)
        {
            int value = tempB[j].first;
            int index = tempB[j].second;
            if(A[i]<=value)
            {
                q.push(A[i]);
                continue;
            }
            result[index] = A[i];
            ++j;
        }
        while(!q.empty())
        {
            for(size_t i =0;i<result.size();++i)
            {
                if(result[i]==0)
                {
                    result[i] =q.front();
                    q.pop();
                }
            }
        }
        
        return result;
    }
};
```