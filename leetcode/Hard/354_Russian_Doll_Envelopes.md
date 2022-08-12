**c++**

```c++
bool pred(vector<int>& a,vector<int>& b){
    if(a[0] ==b[0])
        return a[1]<b[1];
    return a[0]<b[0];
}
class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        if(envelopes.size()==0)
            return 0;
        int* DP = new int[envelopes.size()];
        int h = envelopes.size();
        int w = envelopes[0].size();
        int result =0;
        sort(envelopes.begin(),envelopes.end(),pred);
        for(int i = 0;i<h;++i){
            DP[i] = 1;
            for(int j = 0;j<i;++j){
                if(envelopes[i][0] > envelopes[j][0] && envelopes[i][1] > envelopes[j][1]){
                    DP[i] = max(DP[i], 1+DP[j]);
                }
            }
            result= max(result,DP[i]);
        }
        return result;
    }
};
```