class Solution:
    def genNext(self, n: int) -> int:
        total = 0

        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10

        return total

    def isHappy(self, n: int) -> bool:
        fast = n
        slow = n

        while True:
            slow = self.genNext(slow)
            fast = self.genNext(self.genNext(fast))

            if slow == 1:
                return True

            if slow == fast:
                return False