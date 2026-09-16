class Solution {
public:
    int M = 1e9 + 7; 
    int dp[1001][1001];

    int numberOfSets(int n, int K) {
        // base case
        // k ==0 -> 1(i<n)
        for(int i =0;i<n;i++){
            dp[0][i]=1;
        }

        for(int k = 1;k<=K;k++){

            vector<int> prevRowSum(n+1,0);
            for(int x = n-1;x>=0;x--){
                prevRowSum[x]=(prevRowSum[x+1] + dp[k-1][x]) % M;
            }
            for(int i =n-1;i>=0;i--){
                
                long long take = prevRowSum[i+1];

                long long  skip = dp[k][i+1] % M;

                dp[k][i]= (take + skip) % M;
            }
        }
        return dp[K][0] ; // solve(k,0)
    }
};

