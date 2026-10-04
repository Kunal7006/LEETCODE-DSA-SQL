class Solution:
    #best approach
    def checkValidString(self, s: str) -> bool:
        min =0
        max =0

        for x in s:
            if x == '(':
                min+=1
                max+=1
            if x ==')':
                min -=1
                max -=1
            if x == '*':
                min-=1
                max+=1
            if min <0:
                min =0
            if max <0:
                return False
        return min ==0
