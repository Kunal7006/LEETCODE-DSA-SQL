/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    void reorderList(ListNode* head) {

        if (head == nullptr || head->next == nullptr)
            return;
        ListNode* slow = head;
        ListNode* fast = head;

        while(fast!=nullptr && fast->next!=nullptr){
            slow = slow->next;
            fast = fast->next->next;
        }

        //everse after  slow 

        ListNode* prev = nullptr;
        ListNode* curr = slow->next;
        // disconnect 2nd half
        slow->next = nullptr;

        while(curr!=nullptr){
            ListNode* nxt = curr ->next;

            curr->next = prev;

            prev = curr;
            curr = nxt;
        }

        //merge 2 halfes alternativvely 
        ListNode* first = head;
        ListNode* second = prev ;

        while(second!=nullptr){
            ListNode* firstNext = first->next;
            ListNode* secondNext = second->next;

            first->next = second;
            second->next = firstNext;

            first = firstNext;
            second = secondNext;
        }
        
    }
};