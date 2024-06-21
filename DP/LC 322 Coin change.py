class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #Bottom up approach
        #print("coins", coins)
        #print("amount",amount)
        #edge case that irrespective of no of coins you have what if amount required is 0 -> you dont need any coin
        if amount ==0:
            return 0
        dp = [-1] * (amount + 1) 
        dp[0] = 0
        #if amount = 0, no of coins needed = none (0) -> leave dp[0] = 0 as is
        for i in range(1, amount + 1):
            minanswer = float('inf')
            for coin in coins:
                if coin > i:  # i = 7, coin = 8, 0 ways, 0 already filled
                    continue
                if dp[i - coin] != -1:
                    current_answer = dp[i - coin] + 1
                    minanswer = min(minanswer, current_answer)
            
            dp[i] = minanswer if minanswer != float('inf') else -1

        return dp[amount]
                

        
        