```c++
class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        bool downhill =false;
        for(size_t i=0;i<arr.size()-1;++i)
        {
            if(arr[i]==arr[i+1])
                return false;
            //내리막길
            if(arr[i]>arr[i+1])
                downhill=true;
            if(downhill && i==0)
                return false;
            //오르막길
            if(downhill && arr[i] <=arr[i+1])
                return false;
            
        }
        return downhill;
    }
};
```