class Solution {
public:
//tc = n logn * N
    static int getDigitSum(int num){
        int sum =0;

        while(num){
            int digit = num%10;
            sum+=digit;
            num /=10;
        }
        return sum;
    }
    int minSwaps(vector<int>& nums) {
        int n = nums.size();

        vector<int> afterSorted(nums);

        auto lambda =[](int num1,int num2){
            int num1DigitSum = getDigitSum(num1);
            int num2DigitSum = getDigitSum(num2);
            if(num1DigitSum != num2DigitSum){
                return num1DigitSum < num2DigitSum;
            }
            return num1<num2;

        };

        sort(afterSorted.begin(),afterSorted.end(),lambda);

        unordered_map<int,int> valToIndex;

        for(int i =0;i<n;i++){
            valToIndex[nums[i]]=i;
        }

        int swapCount =0;

        for(int i =0;i<n;i++){
            int expectedVal = afterSorted[i];
            int currVal = nums[i];

            if(expectedVal == currVal ) continue;

            int idx = valToIndex[expectedVal];
            nums[i]=expectedVal;
            nums[idx] = currVal;
            valToIndex[expectedVal]=i;
            valToIndex[currVal]=idx;
            swapCount++;
        }
        return swapCount;
    }
};