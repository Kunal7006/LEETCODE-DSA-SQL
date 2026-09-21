class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result =[0]*k
        prevRemainderCount = [0]*k

        for i in range(n):
            currentRemainderCount=[0]*k

            numRemainder = nums[i] % k
            currentRemainderCount[numRemainder]+=1

            for oldRemainder in range(k):
                newRemainder = (oldRemainder * numRemainder) % k

                currentRemainderCount[newRemainder]+=prevRemainderCount[oldRemainder]
            
            prevRemainderCount = currentRemainderCount

            for remainder in range(k):
                result[remainder]+= prevRemainderCount[remainder]
        
        return result