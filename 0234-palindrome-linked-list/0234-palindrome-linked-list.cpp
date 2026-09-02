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
    ListNode* reverseLL(ListNode* head){
        ListNode* curr = head;
        ListNode* prev = nullptr;

        while(curr!=nullptr){
            ListNode* nxt = curr->next;

            curr->next=prev;
            prev = curr;
            curr = nxt;
        }
        return prev;
    }
public:
    bool isPalindrome(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;

        while(fast!=nullptr && fast->next!= nullptr){
            slow = slow->next;
            fast = fast->next->next;
        }

        slow = reverseLL(slow);

        fast=head;

        while(slow!=nullptr){
            if(slow->val!=fast->val){
                return false;
            }
            slow = slow->next;
            fast = fast->next;
        }

        return true;
    }
};