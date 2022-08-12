```c++
class Solution {
public:
    string simplifyPath(string path) {
        string result, tmp;
        vector<string> tmpvec;
        stringstream str(path);
        while(getline(str,tmp,'/'))
        {
            if(tmp =="." || tmp=="") continue;
            if(tmp==".." && !tmpvec.empty()) tmpvec.pop_back();
            else if(tmp!="..") tmpvec.push_back(tmp);
        }
        for(auto i : tmpvec)
        {
            result+= ("/" + i );
        }
        if(result.empty())
        {
            result +='/';
        }
        return result;
    }
};
```