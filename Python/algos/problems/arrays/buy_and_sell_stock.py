# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Amazon D-E-Shaw Directi Flipkart Goldman Sachs Intuit MakeMyTrip Microsoft Ola Cabs Oracle Paytm Pubmatic Quikr Salesforce Sapient Swiggy Walmart Media.net Google

class Solution:
    def maxProfit(self, prices) -> int:
        max_value = 0
        profit = 0
        for i in reversed(range(len(prices) - 1)):
            buy_price = prices[i]
            potential_sell_price = max(max_value, prices[i + 1])
            if potential_sell_price > buy_price:
                profit = max(max_value, potential_sell_price - buy_price)
            max_value = prices[i]

        return profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit([7, 6, 4, 3, 1]))
print(Solution().maxProfit([1, 2]))
