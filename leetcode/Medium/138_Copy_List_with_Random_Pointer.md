```c++
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    int findrandom(Node* temp,Node* original)
    {
        if(temp->random==nullptr)   
            return -1;// null
        else
        {
            int result=0;

            while(original != temp->random)
            {
                ++result;
                original=original->next;
            }
            return result;
        }
        
    }
    Node* copyRandomList(Node* head) {
        
        Node* newHead;
        //새헤드 노드를 만듦.
        if(head==nullptr)
            return  nullptr;
        else
        {
            newHead = new Node(head->val);
            newHead->next=nullptr;
            newHead->random=nullptr;
            Node* location = newHead;
            Node* tempNode= head;
            if(tempNode->next!=nullptr)
                tempNode=tempNode->next;
            while(tempNode!=nullptr && head->next!=nullptr)
            {
                Node* newNode = new Node(tempNode->val);
                newNode -> next = nullptr;
                newNode -> random = nullptr;
                location->next = newNode;
                tempNode = tempNode->next;
                location = location->next;
            }
            //다시 돌면서 random에 맞게
            location = newHead;
            tempNode=head;
            while(tempNode!=nullptr)
            {
                int indexNum = findrandom(tempNode,head);
                if(indexNum==-1)
                    location->random = nullptr;
                else
                {
                    Node* find = newHead;
                    for(int i=0;i<indexNum;++i)
                    {
                        find=find->next;
                    }
                    location->random = find;
                }
                
                tempNode= tempNode->next;
                location=location->next;
            }
                
            
        }
        return newHead;
    }
};
```