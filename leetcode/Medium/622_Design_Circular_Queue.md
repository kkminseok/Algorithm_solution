**c++**

```c++
class MyCircularQueue {
public:
    list<int> li;
    list<int>::iterator head;
    list<int>::iterator rear;
    int lisize; 
    MyCircularQueue(int k) {
        lisize = k;
    }
    
    bool enQueue(int value) {
        if(li.size()==lisize){
            return false;
        }
        else{
            li.push_back(value);
            if(li.size()==1){
                head = li.begin();
            }
            rear = li.end();
        }
        return true;
    }
    
    bool deQueue() {
        if(li.empty())return false;
        li.erase(head);
        if(!li.empty())
            head = li.begin();
        return true;
    }
    
    int Front() {
        return li.empty() ? -1 : li.front();
    }
    
    int Rear() {
        return li.empty() ? -1 : li.back();
    }
    
    bool isEmpty() {
        return li.size() == 0  ? true : false;
    }
    
    bool isFull() {
        return li.size() == lisize ? true : false;
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */
```