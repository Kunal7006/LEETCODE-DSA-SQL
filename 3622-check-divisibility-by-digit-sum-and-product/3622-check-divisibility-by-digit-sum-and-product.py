class Solution(object):

    def digSum(self, n):
        total = 0

        while n:
            total += n % 10
            n //= 10

        return total

    def digProduct(self, n):
        product = 1

        while n:
            product *= n % 10
            n //= 10

        return product

    def checkDivisibility(self, n):
        a = self.digSum(n)
        b = self.digProduct(n)

        return n % (a + b) == 0