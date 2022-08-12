```c++
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int size = matrix.size();

       for(size_t i =0;i<size;++i)
       {
           vector<int> temp;
           for(int j = size-1;j>-1;--j)
           {
               temp.push_back(matrix[j][0]);
               matrix[j].erase(matrix[j].begin());
           }
           matrix.push_back(temp);    
       }
        for(int i =0 ;i<size;++i)
            matrix.erase(matrix.begin());
    }
};
```