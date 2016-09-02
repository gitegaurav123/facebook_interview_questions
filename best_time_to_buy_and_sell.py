class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_gain = 0
        current_index = len(prices) - 1
        max_value = 0
        while(current_index >=0):
            # print prices[current_index], max_value, max_gain
            if prices[current_index] > max_value:
                max_value = prices[current_index]
            else:
                gain = max_value - prices[current_index]
                if gain > max_gain:
                    max_gain = gain
            current_index -= 1
        return max_gain