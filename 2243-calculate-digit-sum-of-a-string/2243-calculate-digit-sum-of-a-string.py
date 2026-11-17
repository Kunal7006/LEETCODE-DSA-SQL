class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            temp = ""

            for i in range(0,len(s),k):
                sum =0
                for j in range(i,min(i+k,len(s))):
                    sum += ord(s[j]) -ord('0')
                temp += str(sum)
            s=temp
        return s