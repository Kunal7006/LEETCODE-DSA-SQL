class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        n = len(s)
        mp ={}

        for i in range(len(knowledge)):
            mp[knowledge[i][0]]= knowledge[i][1]
        
        result = ""

        i =0

        while i <n:
            if s[i]=='(':
                j = s.find(")",i+1)
                temp = s[i+1:j]
                if temp in mp:
                    result+= mp[temp]
                else:
                    result+="?"
                i=j
            else:
                result+=s[i]
            i+=1
        return result
