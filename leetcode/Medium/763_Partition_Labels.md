**c++**

```c++
class Solution {
public:
    vector<int> partitionLabels(string S) {
        vector<int> charIdx(26,0);
        for(int i = 0 ; i<S.size();++i){
            charIdx[S[i]-'a'] = i;
        }
        
        int maxIdx = -1, lastIdx = 0 ;
        vector<int> res;
        for(int i = 0 ; i <S.size();++i){
            maxIdx = max(maxIdx,charIdx[S[i]-'a']);
            if(maxIdx == i ){
                res.push_back(maxIdx - lastIdx+1);
                lastIdx = i +1;
            }
        }
        return res;
    }
};
```