```c++
class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        vector<int> arr2;
        for(size_t i =0;i<arr.size();++i)
        {
            if(arr[i]==0)
                arr2.push_back(0);
            arr2.push_back(arr[i]);
            arr[i]=arr2[i];
        }
        
    }
};
```
