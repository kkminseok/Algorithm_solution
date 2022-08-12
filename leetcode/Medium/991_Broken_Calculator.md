```c++
class Solution {
public:
    
    int brokenCalc(int X, int Y) {
        queue<pair<int,int>> q;
        q.push(make_pair(Y,0));
        if(Y<X)
            return X-Y;
        while(!q.empty())
        {
            int now = q.front().first;
            int count = q.front().second;
            q.pop();
            if(now<X)
                return count+X-now;
            if(now == X)
                return count;
            if(now%2==0)
                q.push(make_pair(now/2,count+1));
            else
                q.push(make_pair(now+1,count+1));

        }
        return 0;
        
    }
};
```