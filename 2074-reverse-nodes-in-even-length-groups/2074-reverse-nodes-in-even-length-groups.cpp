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
    int reverse(ListNode* last,ListNode* headOfGroup,int n){
        ListNode* prev = nullptr;
        ListNode* curr = headOfGroup;
        ListNode* nextNode = curr->next;
        int count =0;

        while(curr !=nullptr && n>0){
            nextNode = curr->next;

            curr->next = prev;
            prev = curr;
            curr = nextNode;
            n--;
            count++;
        }
        headOfGroup->next = nextNode;
        last->next = prev;
        return count;
    }
    ListNode* reverseEvenLengthGroups(ListNode* head) {
        int gn =0;
        int elementsInPrevGroup =0;
        ListNode* curr = head;
        ListNode* lastOfPrevGroup = nullptr;
        ListNode* lastOfEvenGroup = nullptr;

        while(curr!=nullptr){
            gn++;
            if(gn%2==0){
                elementsInPrevGroup = reverse(lastOfPrevGroup,curr,gn);
                lastOfEvenGroup = curr;
                curr = curr->next;
            }else{
                int k = gn;
                elementsInPrevGroup =0;
                while(curr!=nullptr && k>0){
                    lastOfPrevGroup = curr;
                    curr = curr->next;
                    k--;
                    elementsInPrevGroup++;
                }
            }
        }

        if(gn % 2 ==1 && elementsInPrevGroup %2 ==0){
            reverse(lastOfEvenGroup,lastOfEvenGroup->next,elementsInPrevGroup);
        }else if(gn % 2 ==0 && elementsInPrevGroup %2 ==1){
            reverse(lastOfPrevGroup,lastOfPrevGroup->next,elementsInPrevGroup);
        }
        return head;
    }
};