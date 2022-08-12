```c++
class Solution {
public:
    int reverse(int x) {
        if(x==0 || x>2147483647 || x<-2147483647)
            return 0;
        string temp = "";
        bool check = false;
        if(x<0)
        {
            x= -x;
            check = true;
        }
        temp = to_string(x);
        if(check)
            temp+="-";
        std::reverse(temp.begin(),temp.end());
        long long result = stol(temp);
        if(result>INT_MAX || result<INT_MIN)
            return 0;
        return result;
    }
};
```