**c++**

```c++
class Solution {
public:
    int titleToNumber(string columnTitle) {
        int result = 0 ;
        int pownum = 0;
        for(int i = columnTitle.size()-1;i>=0;--i){
            result+= (pow(26,pownum++) * (columnTitle[i]-64) );
        }
        return result;
        
    }
};
```