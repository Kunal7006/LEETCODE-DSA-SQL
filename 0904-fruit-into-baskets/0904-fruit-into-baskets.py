class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        mp = {}
        l=0
        r=0
        maxFruits = 0

        while r<n:
            mp[fruits[r]]= mp.get(fruits[r],0)+1

            if len(mp)>2:
                mp[fruits[l]]-=1
                if mp[fruits[l]]==0:
                    del mp[fruits[l]]
                l+=1
            maxFruits = max(maxFruits,r-l+1)
            r+=1
        
        return maxFruits