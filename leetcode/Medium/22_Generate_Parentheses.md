```c++
class Solution {
public:
    vector<string> result;
    void solution(int head,int tail,int n,string temp)
    {
        if(temp.size()==n*2 )
        {
            result.push_back(temp);
        }
        else
        {
            if(head<n)
                solution(head+1,tail,n,temp+'(');
            if(tail<head)
                solution(head,tail+1,n,temp+')');   
        }
    }
    vector<string> generateParenthesis(int n) {;
        solution(0,0,n,"");
        
        return result;
    }
};
```