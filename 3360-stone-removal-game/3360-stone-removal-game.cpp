class Solution {
public:
    bool canAliceWin(int n) {
        bool flag=false;
        if(n<10){
            return flag;
        }
        int last = 10;
        n = n-last;
        flag = true;
        while(n>=last-1){
            flag=!flag;
            last = last-1;
            n=n-last;
        }
        return flag;

    }
};