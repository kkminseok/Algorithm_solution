**c++**

```c++
class MyHashMap {
    vector<list<pair<int,int>>> vec;
    size_t vecSize = 10000;
    
public:
    /** Initialize your data structure here. */
    MyHashMap() {
        vec.resize(vecSize);
        
    }
    
    /** value will always be non-negative. */
    void put(int key, int value) {
        list<pair<int,int>> &list = vec[key % vecSize];
        for (auto & val : list) {
            if (val.first == key) {
                val.second = value;
                return;
            }
        }
        list.emplace_back(key, value);
    }
    
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    int get(int key) {
        const auto &list = vec[key % vecSize];
        if (list.empty()) {
            return -1;
        }
        for (const auto & val : list) {
            if (val.first == key) {
                return val.second;
            }
        }
        return -1;
    }
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    void remove(int key) {
        list<pair<int,int>> &pairs = vec[key%vecSize];
        for(auto i=pairs.begin(); i!= pairs.end(); i++)
        {
            if(i->first==key) { pairs.erase(i); return; }
        }
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */


```

-----  

**python**

```python
# using just arrays, direct access table
# using linked list for chaining

class ListNode:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 1000;
        self.h = [None]*self.m
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        index = key % self.m
        if self.h[index] == None:
            self.h[index] = ListNode(key, value)
        else:
            cur = self.h[index]
            while True:
                if cur.pair[0] == key:
                    cur.pair = (key, value) #update
                    return
                if cur.next == None: break
                cur = cur.next
            cur.next = ListNode(key, value)
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key % self.m
        cur = self.h[index]
        while cur:
            if cur.pair[0] == key:
                return cur.pair[1]
            else:
                cur = cur.next
        return -1
            
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        index = key % self.m
        cur = prev = self.h[index]
        if not cur: return
        if cur.pair[0] == key:
            self.h[index] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.pair[0] == key:
                    prev.next = cur.next
                    break
                else:
                    cur, prev = cur.next, prev.next
                


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
```