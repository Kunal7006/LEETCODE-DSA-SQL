class Solution {
    int nextIndex(int i , vector<int>& nums){
        int n = nums.size();
        return (( i + nums[i]) % n + n) % n;
    }
public:
    bool circularArrayLoop(vector<int>& nums) {
        int n = nums.size();

        for(int i =0;i<n;i++){

            // already visited 
            if (nums[i]==0){
                continue;
            }

            bool positive = nums[i]>0;

            int fast = i;
            int slow = i;

            while(true){

                int nextSlow = nextIndex(slow,nums);

                // direction must remain same 
                if(nums[nextSlow] == 0 || (nums[nextSlow] > 0 ) != positive){
                    break;
                }

                // self loop
                if(slow == nextSlow){
                    break;
                }

                slow = nextSlow;

                int nextFast = nextIndex(fast,nums);
                if(nums[nextFast] == 0 || (nums[nextFast] > 0) != positive || nextFast == fast){
                    break;
                }
                fast = nextFast;

                nextFast = nextIndex(fast,nums);
                if(nums[nextFast] == 0 || (nums[nextFast] > 0 ) != positive || nextFast == fast){
                    break;
                }

                fast = nextFast;

                if(slow == fast){
                    return true;
                }

                
            }

            // mark path as visited
            int curr = i;

            while(nums[curr]!=0 && (nums[curr]>0) == positive){
                int next = nextIndex(curr,nums);

                if(nums[next] ==0 || (nums[next]>0) != positive || next == curr){
                    break;
                } 

                nums[curr]=0;

                curr = next;
            }

            if(nums[curr] !=0 && (nums[curr]>0) == positive){
                nums[curr] =0;
            }

        }
        return false;
    }
};