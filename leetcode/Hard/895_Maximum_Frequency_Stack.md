```c++
class FreqStack {
private:
    unordered_map<int,int> map;
    vector<pair<int,int>> st;
    vector<int> vec;
    int maxnum=0;
    
public:
    FreqStack() {
        vec.push_back(0);
    }
    
    void push(int x) {
        if(map.find(x) == map.end())
        {
            map[x]=1;
            if(maxnum==0)
            {
                maxnum=1;
                vec.push_back(1);
            }
            else
            {
                vec[1]++;
            }
        }
        else
        {
            map[x]++;
            if(map[x]>maxnum)
            {
                maxnum=map[x];
                if(vec.size()<=maxnum)
                    vec.push_back(1);
                else
                {
                    vec[maxnum]++;
                }
            }
            else
                vec[map[x]]++;
        }
        st.push_back(make_pair(x,map[x]));
    }
    
    int pop() {
        int size = st.size()-1;
        int temp = st[size].first;
        if(map[temp] == maxnum)
        {
            map[temp]--;
            st.pop_back();
            vec[maxnum]--;
            if(vec[maxnum]==0)
            {
                --maxnum;
            }
            return temp;
        }
        else
        {
            for(;size>=0;--size)
            {
                if(st[size].second == maxnum)
                {
                    map[st[size].first]--;
                    int returnnum = st[size].first;
                    st.erase(st.begin() + size);
                    vec[maxnum]--;
                    if(vec[maxnum]==0)
                    {
                        --maxnum;
                    }
                    return returnnum;
                }
            }
        }

        return 1;
    }
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 */
```