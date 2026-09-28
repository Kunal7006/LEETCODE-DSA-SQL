class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        n = len(text)
        mp ={}

        for i in range(n):
            if text[i] not in mp:
                mp[text[i]]=0
            mp[text[i]]+=1
        
        ans = float('inf')
        if 'b' in mp:
            ans = min(ans,mp['b'])
        else:
            return 0
        if 'a' in mp:
            ans = min(ans,mp['a'])
        else:
            return 0
        if 'l' in mp:
            ans = min(ans,mp['l']//2)
        else:
            return 0
        if 'o' in mp:
            ans = min(ans,mp['o']//2)
        else:
            return 0
        if 'n' in mp:
            ans = min(ans,mp['n'])
        else:
            return 0

        return ans


