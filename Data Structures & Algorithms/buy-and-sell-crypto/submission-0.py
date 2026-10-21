class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        # find largest diff in arr
        # have running total, and update?

        local_low = float(inf)
        local_high = float(-inf)
        profit = float(-inf)

        for i in range(len(prices)):
            # if changing the high point increases profit
            # change high

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


            


        