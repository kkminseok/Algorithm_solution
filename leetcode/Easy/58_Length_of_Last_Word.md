**c++**

```c++
class Solution {
public:
    int lengthOfLastWord(string s) {
        int count = 0;
        int res = 0 ;
        for(int i = 0 ; i<s.size();++i){
            if(s[i] ==' '){
                count=0;
                continue;
            }
            ++count;
            res =count;
        }
        return res;
    }
};
```