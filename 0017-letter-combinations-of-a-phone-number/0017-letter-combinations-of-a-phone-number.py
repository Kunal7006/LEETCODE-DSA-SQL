class Solution:
    def __init__(self):
        self.result=[]
    def solve(self,idx,digits,temp,mp):
        if idx>=len(digits):
            self.result.append(temp)
            return 
        ch = digits[idx]
        string = mp[ch]

        for ch in string:
            temp+=ch
            self.solve(idx+1,digits,temp,mp)
            temp = temp[:-1]
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits)==0:
            return self.result
        
        mp ={}
        mp['2']="abc"
        mp['3']="def"
        mp['4']="ghi"
        mp['5']="jkl"
        mp['6']="mno"
        mp['7']="pqrs"
        mp['8']="tuv"
        mp['9']="wxyz"
        temp =""

        self.solve(0,digits,temp,mp)
        return self.result