class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum>num*9:
            return ""
        nines = sum//9
        remain = sum%9

        result = "9" * nines

        if remain>0:
            result = result + str(remain)
        
        result += "0"*(num-len(result))
        return result