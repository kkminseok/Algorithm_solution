```c++
class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
     for(size_t i =arr.size()-1;i>0;--i)
     {
         if(arr[i] > arr[i-1])
         {
             arr[i-1]=arr[i];
         }
     }
        arr.erase(arr.begin());
        arr.push_back(-1);
        return arr;     
    }

};
```