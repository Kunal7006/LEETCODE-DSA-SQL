
class Solution:
    # KMP Start
    def computeLPS(self, pattern, lps):
        M = len(pattern)
        length = 0
        lps[0] = 0

        i = 1
        while i < M:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

    def KMPSearch(self, pat, txt):
        N = len(txt)
        M = len(pat)

        lps = [0] * M
        self.computeLPS(pat, lps)

        i = 0  # index for text
        j = 0  # index for pattern

        while i < N:
            if pat[j] == txt[i]:
                i += 1
                j += 1

            if j == M:
                return True  # pattern found
            elif i < N and pat[j] != txt[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return False
    # KMP End

    def isRotationPossible(self, vec1, vec2):
        text = vec2[:]
        text.extend(vec2)

        return self.KMPSearch(vec1, text)

    def sortableIntegers(self, nums):
        n = len(nums)

        sorted_nums = sorted(nums)

        result = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for start in range(0, n, k):
                vec1 = nums[start:start + k]
                vec2 = sorted_nums[start:start + k]

                if not self.isRotationPossible(vec1, vec2):
                    valid = False
                    break

            if valid:
                result += k

        return result
