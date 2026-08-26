class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ones = []

        # Store positions of all '1's
        for i, ch in enumerate(s):
            if ch == '1':
                ones.append(i)

        # Not enough 1s
        if len(ones) < k:
            return ""

        min_len = float('inf')
        answer = ""

        # Check every group of k consecutive 1s
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]

            substring = s[start:end + 1]
            length = len(substring)

            if length < min_len:
                min_len = length
                answer = substring

            elif length == min_len and substring < answer:
                answer = substring

        return answer