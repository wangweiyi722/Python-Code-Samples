# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 15:08:20 2018

@author: wangw
"""

def calc_max_profit(prices):
    if len(prices) < 2:
        raise ValueError("need at least two prices")
    max_profit = prices[1] - prices[0]
    min_price = min(prices[1], prices[0])
    
    idx = 2
    while idx < len(prices):
        max_profit = max(max_profit, prices[idx] - min_price)
        min_price = min(prices[idx], min_price)
        idx += 1

    return max_profit            

def main():
    # Calculate the max profit given a time associated array of values
    test1 = [10]
    result1 = calc_max_profit(test1)
    print(result1)
    
main()