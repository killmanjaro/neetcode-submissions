class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # first attempt
        '''
        # find largest diff in arr
        # have running total, and update?

        local_low = float(inf)
        local_high = float(-inf)
        profit = 0 # profit
        index_buy = 0

        for i in range(len(prices)): # i is the selling price
            # if changing the high point increases profit
            # change high

        '''


        # brute force
        '''
        local_low = float('inf')
        local_high = float('-inf')
        profit = 0

        # brute force
        # i is sell index
        for i in range(len(prices)):
            # j is buy index
            for j in range(len(prices)):
                if (j < i):
                    if prices[i] - prices[j] > profit:
                        profit = prices[i] - prices[j]
                    
        return profit
        '''

        # solution
        l = 0 # left ptr (buying)
        r = 1 # right ptr (selling)
        max_profit = 0

        while r < len(prices):
            # profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            else:
                l = r # found a low price
            r += 1
        return max_profit



            


        