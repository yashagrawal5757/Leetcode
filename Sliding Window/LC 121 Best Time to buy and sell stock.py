class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Postfix technique : TC = o(n), SC = O(n)
        '''
        postfix = [0] * len(prices)
        for i in range(len(prices)-2, -1,-1):
            postfix[i] = max(postfix[i+1],prices[i+1])
        differences = []
        max_difference = 0
        for i in range(0,len(postfix)):
            difference = postfix[i] - prices[i]
            max_difference = max(max_difference, difference)

        return max_difference     
        '''
        #Sliding window : TC = O(n), SC = O(1)
        i,j = 0,1
        maxprofit = 0
        while(j<len(prices)):
            profit = prices[j] - prices[i]
            if profit<=0:
                i = j
                j+= 1
            else:
                maxprofit = max(maxprofit,profit)
                j+= 1
                #if a no lower than ith comes it will automatically go to if & move i to j
        return maxprofit

        