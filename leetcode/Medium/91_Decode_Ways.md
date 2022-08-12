**c++**

```c++
class Solution {
public:
    int numDecodings(string s) {   
        if(s[0]=='0')
            return 0;
        if(s.size()==1) {
            return 1;
        }
        int* DP= new int[s.size()+1];
        DP[0]=1;
        DP[1]=1;
        for(size_t i =2;i<=s.size();++i){
            if(s[i-1]!='0')
                DP[i] = DP[i-1];
            else
                DP[i]=0;
            string temp ="";        
            temp+=s[i-2];
            temp+=s[i-1];
            int con = stoi(temp);
            if(con<=26 && con>=10)
                DP[i] += DP[i-2];  
        }
        
        return DP[s.size()];
    }
};
```