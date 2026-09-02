class Solution:
    def getNext(self, n):
        total = 0

        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10

        return total

    def isHappy(self, n):
        seen = set()

        while n != 1:
            # If n is already seen, we are in a cycle
            if n in seen:
                return False

            seen.add(n)

            n = self.getNext(n)

        return True