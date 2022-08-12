**c++**

```c++
class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int ans = 0 ;
        for(int i = 0 ; i < k; ++i){
            ans += cardPoints[i];
        }
        if(k == cardPoints.size())
            return ans;
        
        int pick = 1;
        int right = cardPoints.size()-1;
        priority_queue<int> pq;
        pq.push(ans);
        while(pick <= k){
            ans -= cardPoints[k - pick] ;
            ans += cardPoints[right--];
            ++pick;
            pq.push(ans);
        }
        
        return pq.top();
        
    }
};
```