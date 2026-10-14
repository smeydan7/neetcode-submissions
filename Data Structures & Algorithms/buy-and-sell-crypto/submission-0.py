class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        if len(prices) == 2:
            if prices[1] >= prices[0]:
                return prices[1] - prices[0]
        
        l_min_value = prices[0]
        l_min = [0] * len(prices)
        profits = [0] * len(prices)
        for i in range(len(prices)):
            if prices[i] < l_min_value:
                l_min_value = prices[i]
            l_min[i] = l_min_value

            pot = prices[i] - l_min[i]
            if pot <= 0:
                continue
            else: 
                profits[i] = prices[i] - l_min[i]
        print(l_min)
        print(profits)


        if l_min == prices:
            return 0
        
        return max(profits)