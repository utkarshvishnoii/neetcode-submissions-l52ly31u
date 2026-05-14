class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(amount):
            if amount in dp:
                return dp[amount]

            if amount == 0:
                return 0

            res = float("inf")

            for coin in coins:
                if amount - coin >= 0:
                    temp = dfs(amount - coin)

                    if temp != -1:
                        res = min(res, 1 + temp)

            dp[amount] = -1 if res == float("inf") else res
            return dp[amount]

        return dfs(amount)