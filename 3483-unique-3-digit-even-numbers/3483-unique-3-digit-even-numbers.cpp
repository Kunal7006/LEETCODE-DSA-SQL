class Solution {
public:
    int totalNumbers(vector<int>& digits) {
        int n = digits.size();
        int totalEven =0;
        vector<int> digitCount(10,0);

        for(int i =0;i<n;i++){
            digitCount[digits[i]]++;
        }

        for(int i =1;i<=9;i++){
            if(digitCount[i]==0){
                continue;
            }
            digitCount[i]--;
            for(int j =0;j<=9;j++){
                if(digitCount[j]==0){
                    continue;
                }
                digitCount[j]--;

                for(int k =0;k<=8;k+=2){
                    if(digitCount[k]==0){
                        continue;
                    }

                    totalEven++;
                }
                digitCount[j]++;
            }
            digitCount[i]++;

        }
        return totalEven;
    }
};