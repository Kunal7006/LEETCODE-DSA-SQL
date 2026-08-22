class Solution {
public:
    bool checkDivisibility(int n) {
        int product =1,sum =0;
        int a =n;

        while(a){
            sum += a%10;
            product *= a%10;
            a=a/10;
        }

        return n%(sum+product)==0;
        

    }
};