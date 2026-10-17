class Solution:
    def getDigitSum(self, num: int) -> int:
        sum = 0

        while num:
            digit = num % 10
            sum += digit
            num //= 10

        return sum

    def minSwaps(self, nums: list[int]) -> int:
        n = len(nums)

        afterSorted = nums.copy()

        def lambda_func(num1, num2):
            num1DigitSum = self.getDigitSum(num1)
            num2DigitSum = self.getDigitSum(num2)

            if num1DigitSum != num2DigitSum:
                return num1DigitSum < num2DigitSum

            return num1 < num2

        afterSorted.sort(key=lambda num: (self.getDigitSum(num), num))

        valToIndex = {}

        for i in range(n):
            valToIndex[nums[i]] = i

        swapCount = 0

        for i in range(n):
            expectedVal = afterSorted[i]
            currVal = nums[i]

            if expectedVal == currVal:
                continue

            idx = valToIndex[expectedVal]

            nums[i] = expectedVal
            nums[idx] = currVal

            valToIndex[expectedVal] = i
            valToIndex[currVal] = idx

            swapCount += 1

        return swapCount