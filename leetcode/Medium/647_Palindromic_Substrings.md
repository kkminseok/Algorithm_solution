**c++**

```c++
class Solution {
public:
    bool check(string s,int left,int right){
        while(left<=right){
            if(s[left]!=s[right])
                return false;
            ++left;
            --right;
        }
        return true;
    }
    int countSubstrings(string s) {
        int result = 0;
        for(size_t i =0;i<s.size();++i){
            for(size_t j = i ;j<s.size();++j){
                if(check(s,i,j)){
                    ++result;
                }
            }
        }
        return result;
    }
};
```