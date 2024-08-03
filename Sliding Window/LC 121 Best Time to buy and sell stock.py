class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j = 0,1
        profit = 0
        while(j<len(prices)):
            if (prices[i]> prices[j]):
                i+= 1
                if (i==j):
                    j += 1
            else:
                #answer
                profit = max(prices[j] - prices[i], profit)
                j+= 1
        return profit
        


        