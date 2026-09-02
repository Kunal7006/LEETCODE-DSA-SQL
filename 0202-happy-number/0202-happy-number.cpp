class Solution {
    int genNext(int n ){
        int sum =0;
        while(n){
            int digit = n % 10;
            sum += digit * digit;
            n = n/10;
        }
        return sum;
    }
public:
    bool isHappy(int n) {
        int fast = n;
        int slow = n;

        while(1){
            slow = genNext(slow);
            fast = genNext(genNext(fast));

            if(slow == fast){
                break;
            }
            if(slow == 1){
                break;
            }

        }

        return slow ==1;

    }
};