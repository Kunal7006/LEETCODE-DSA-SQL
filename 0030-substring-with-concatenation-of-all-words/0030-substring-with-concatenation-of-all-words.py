class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        wordLen = len(words[0])
        wordCount = len(words)
        ans = []

        totalLength = wordLen * wordCount

        if totalLength > n :
            return ans
        
        required = {}

        for i in range(wordCount):
            if words[i] not in required:
                required[words[i]] = 0

            required[words[i]] += 1
        
        for offset in range(wordLen):

            l =offset
            r =offset

            current = {}
            count =0

            while r+wordLen <=n:
                word = s[r:r+wordLen]
                r+= wordLen

                if word not in required:
                    current.clear()
                    count =0
                    l=r

                else :

                    if word not in current:
                        current[word] =0
                    current[word]+=1
                    count +=1

                    while current[word] > required[word]:
                        leftWord = s[l:l+wordLen]
                        current[leftWord]-=1
                        count-=1
                        l+=wordLen
                    
                    if count == wordCount:

                        ans.append(l)
                        leftWord = s[l:l+wordLen]
                        current[leftWord]-=1
                        count -=1
                        l+=wordLen
        
        return ans 
