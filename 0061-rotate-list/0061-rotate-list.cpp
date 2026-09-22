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
    ListNode* rotateRight(ListNode* head, int k) {

        if(head==NULL || head->next==NULL || k==0){
            return head;
        }

        ListNode* temp = head;
        int d=1;
        while(temp->next !=NULL){
            temp = temp->next;
            d++;
        }

        k=k%d;
        temp->next= head;

        int end = d-k;

        while(end--){
            temp=temp->next;
        }
        head=temp->next;
        temp->next = NULL;
        return head;

        // ListNode* newHead = NULL;

        // for(int i=0;i<k;i++){
        //     head=head->next;
        // }
        // newHead = head->next;

        // head->next=NULL;

        // return newHead;
        
    }
};