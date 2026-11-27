class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        copies =[0]*n

        minPrice = float('inf')

        for i in range(n):
            minPrice = min(minPrice,items[i][1])
            copy =0
            for j in range(n):
                if i == j:
                    continue
                if items[j][0]%items[i][0]==0:
                    copy+=1
            copies[i]=copy
        
        t=[[0]*(budget+1) for _ in range(n+1)]

        for b in range(budget+1):
            t[0][b]=b//minPrice
        
        for i in range(1,n+1):
            for b in range(budget+1):
                price = items[i-1][1]
                take =0

                if price <= b:
                    take = 1+copies[i-1]+t[i-1][b-price]
                skip = t[i-1][b]

                t[i][b]=max(take,skip)
        
        return t[n][budget]