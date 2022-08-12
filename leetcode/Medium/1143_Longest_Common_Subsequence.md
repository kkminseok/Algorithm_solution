**c++**
```c++
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int** check;
        int row = text1.size()+1;
        int col = text2.size()+1;
        check=new int*[row * sizeof(int)];
        for(int i =0;i<row;++i)
            check[i] = new int[col * sizeof(int)];
        for(int i = 0;i<row;++i)
        {
            for(int j = 0 ;j<col;++j)
            {
                if(i==0 || j==0 )
                {
                    check[i][j] = 0;
                    continue;
                }
                if(text1[i-1] ==text2[j-1])
                {
                    check[i][j]= check[i-1][j-1]+1;
                }
                else
                    check[i][j] = max(check[i-1][j],check[i][j-1]);
            }
        }
        return check[row-1][col-1];
            
    }
};
```