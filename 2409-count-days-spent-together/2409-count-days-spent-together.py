class Solution:
    def toDay(self,s,arr):
        month = int(s[0:2])
        day = int(s[3:5])

        return (0 if month==1 else arr[month-2])+day
        
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        arr =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        curr =0
        for i in range(len(arr)):
            curr+=arr[i]
            arr[i]=curr
        
        start_alice = self.toDay(arriveAlice,arr)
        end_alice = self.toDay(leaveAlice,arr)
        start_bob = self.toDay(arriveBob,arr)
        end_bob = self.toDay(leaveBob,arr)

        start = max(start_alice,start_bob)
        end = min(end_alice,end_bob)

        return max(0,end-start+1)