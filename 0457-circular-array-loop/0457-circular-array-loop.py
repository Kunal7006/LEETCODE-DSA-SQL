class Solution:
    def nextIndex(self,i,nums):
        n = len(nums)
        return (i+nums[i])%n

    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n):

            if nums[i]==0:
                continue
            
            positive = nums[i]>0

            fast =i
            slow = i
            while(True):

                nextSlow = self.nextIndex(slow,nums)

                if nums[nextSlow] == 0 or (nums[nextSlow]>0) != positive or slow == nextSlow:
                    break
                
                slow = nextSlow

                nextFast = self.nextIndex(fast,nums)

                if nums[nextFast] ==0 or (nums[nextFast]>0) != positive or fast == nextFast:
                    break
                
                fast = nextFast

                nextFast = self.nextIndex(fast,nums)

                if nums[nextFast] ==0 or (nums[nextFast]>0) != positive or fast == nextFast:
                    break
                
                fast = nextFast

                if slow == fast:
                    return True
            
            curr = i

            while nums[curr] !=0 and (nums[curr]>0)== positive:
                nxt = self.nextIndex(curr,nums)

                if nums[nxt] == 0 or (nums[nxt]>0) != positive or curr == nxt:
                    break
                nums[curr]=0
                curr = nxt
            
            if nums[curr] >=0 and nums[curr]>0 == positive:
                nums[curr]=0
        return False