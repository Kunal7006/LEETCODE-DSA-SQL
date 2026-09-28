class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mp1 ={}
        mp2 ={}

        for i in range(len(ransomNote)):
            if ransomNote[i] not in mp1:
                mp1[ransomNote[i]] =0
            mp1[ransomNote[i]]+=1

        for i in range(len(magazine)):
            if magazine[i] not in mp2:
                mp2[magazine[i]] =0
            mp2[magazine[i]]+=1
        
        ans = True

        for key,value in mp1.items():
            if key in mp2:
                if value > mp2[key]:
                    ans = False
                    break
            else:
                return False
            
        return ans
        