class Solution {
public:
    int maximumSaleItems(vector<vector<int>>& items, int budget) {

        int n = items.size();

        vector<int> freq(n + 1, 0);
        vector<int> copies(n + 1, 0);

        long long minPrice = INT_MAX;
        long long money = budget;
        long long ans = 0;

        // Step 1: Calculate frequency and minimum price
        for(auto& item : items) {
            freq[item[0]]++;
            minPrice = min(minPrice, (long long)item[1]);
        }

        // Step 2: Count eligible free copies using multiples
        for(int i = 1; i <= n; i++) {

            if(freq[i] == 0) continue;

            for(int j = i; j <= n; j += i) {
                copies[i] += freq[j];
            }

            // Exclude the item itself
            copies[i]--;
        }

        // Step 3: Sort items by price
        sort(items.begin(), items.end(),
             [](const auto& a, const auto& b) {
                 return a[1] < b[1];
             });

        // Step 4: Make beneficial bonus purchases
        for(auto& item : items) {

            int factor = item[0];
            long long price = item[1];

            if(price >= 2 * minPrice) {
                break;
            }

            long long buy = min(
                (long long)copies[factor],
                money / price
            );

            ans += 2 * buy;
            money -= buy * price;
        }

        // Step 5: Spend remaining budget on cheapest item
        ans += money / minPrice;

        return ans;
    }
};