#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest
number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Determines the fewest
    number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    coins.sort(reverse=True)

    for coin in coins:
        for i in range(coin, total + 1):
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
            else:
                break

    if dp[total] > total:
        return -1
    else:
        return dp[total]
