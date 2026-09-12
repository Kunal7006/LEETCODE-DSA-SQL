class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n= len(digits)
        totalEven = 0
        digitCount = [0]*10

        for i in range(n):
            digitCount[digits[i]]+=1
        
        for i in range(1,10):
            if digitCount[i]==0:
                continue
            digitCount[i]-=1

            for j in range(10):
                if digitCount[j]==0:
                    continue
                digitCount[j]-=1

                for k in range(0,9,2):
                    if digitCount[k]==0:
                        continue
                    totalEven+=1
                digitCount[j]+=1
            digitCount[i]+=1
        return totalEven