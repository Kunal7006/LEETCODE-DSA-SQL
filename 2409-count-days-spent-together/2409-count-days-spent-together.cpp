class Solution {
public:
    int toDay(string s, vector<int>& prefix) {
        // 08-15 ->227
        int month = stoi(s.substr(0, 2));
        int day = stoi(s.substr(3, 2));

        return (month == 1 ? 0 : prefix[month - 2]) + day;
    }
    int countDaysTogether(string arriveAlice, string leaveAlice,
                          string arriveBob, string leaveBob) {
        vector<int> arr = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        int curr = 0;
        for (int i = 0; i < arr.size(); i++) {
            curr += arr[i];
            arr[i] = curr;
        }

        int start_alice = toDay(arriveAlice, arr);
        int end_alice = toDay(leaveAlice, arr);
        int start_bob = toDay(arriveBob, arr);
        int end_bob = toDay(leaveBob, arr);

        int start = max(start_alice,start_bob);
        int end = min(end_alice,end_bob);

        return max(0,end-start+1);
    }
};