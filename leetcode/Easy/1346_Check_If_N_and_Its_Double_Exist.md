```c++
class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        unordered_map<int, int> v;
        
        for(int i=0;i<arr.size();i++){
            
            if(arr[i]%2==0 && v.find((arr[i]/2))!=v.end()){
                return true;
            }
            
            if(v.find((arr[i]*2))!=v.end()){
                return true;
            }
                        if(v.find(arr[i])==v.end()){
                //not present
                            cout<<arr[i];
                v[arr[i]] = 1;
            }
        }
        return false;
    }
};
```