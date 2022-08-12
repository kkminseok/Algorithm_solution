**c++**

```c++
class Solution {
public:
    int minDistance(string word1, string word2) {
        //LCS
        int size1 = word1.size();
        int size2 = word2.size();
        int** DP = new int*[size1+1];
        for(int i = 0 ; i<=size1;++i)
            DP[i] = new int[size2+1];
        
        for(int i = 0 ; i <=size1;++i)
            DP[i][0] = 0;
        for(int j = 0 ; j <=size2;++j)
            DP[0][j] = 0;
        
        for(int i = 1 ; i <=size1;++i){
            for(int j = 1 ; j <=size2;++j){
                    if(word1[i-1] == word2[j-1])
                        DP[i][j] = DP[i-1][j-1] + 1;
                    else
                        DP[i][j] = max(DP[i-1][j],DP[i][j-1]);
                }
            }
            return size1 + size2 - (DP[size1][size2] *2);   
    }
};
```