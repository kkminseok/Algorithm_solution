**python**

```python
class MinStack:

    def __init__(self):
        self.st = []
        """
        initialize your data structure here.
        """
        

    def push(self, x: int) -> None:
        currmin = self.getMin()
        
        if currmin == None or x < currmin : 
            currmin = x
        self.st.append((x,currmin))
        

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        if len(self.st) == 0 :
            return None
        return self.st[len(self.st) -1][0]

    def getMin(self) -> int:
        if len(self.st) == 0 :
            return None
        return self.st[len(self.st)-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

-----  

**c++**

```c++
class MinStack {
private:
    multiset<int> ms;
    stack<int> st;
public:
    /** initialize your data structure here. */
    MinStack() {
    }
    void push(int x) {
        st.push(x);
        ms.insert(x);
    }
    
    void pop() {
        int temp = st.top();
        st.pop();
        auto findindex = ms.find(temp);
        if(findindex!=ms.end())
        {
            ms.erase(findindex);
        }
            
    }
    
    int top() {
        return st.top();
    }
    
    int getMin() {
        multiset<int>::iterator iter = ms.begin();
        return *iter;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
```