# 901. Online Stock Span
# Medium
# Topics
# Companies
# Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

# The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

# For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
# Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.
# Implement the StockSpanner class:

# StockSpanner() Initializes the object of the class.
# int next(int price) Returns the span of the stock's price given that today's price is price.

class StockSpanner:
    def __init__(self):
        self.stack = []
# This method calculates the span of a stock's price. The span is the number of consecutive days the price was less than or equal to the current price.

# Here's a step-by-step breakdown:

# 1. Initialize `span` to 1, assuming the current price is the first day.
# 2. While the stack is not empty and the top price is less than or equal to the current price:
#    - Add the span of the top price to the current span.
#    - Remove the top price from the stack.
# 3. Push the current price and its span onto the stack.
# 4. Return the calculated span.

# This implementation uses a stack to keep track of prices and their corresponding spans, allowing for efficient calculation of the current span.
    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span