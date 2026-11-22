class Solution:
    def checkString(self, s: str) -> bool:
        n = len(s)

        if "ba" in s:
            return False
        else:
            return True
