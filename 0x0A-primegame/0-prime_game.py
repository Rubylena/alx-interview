#!/usr/bin/python3
''' Prime Game Center'''


def isWinner(x, nums):
    ''' function to check the winner '''

    winner_count = {"Maria": 0, "Ben": 0}

    for n in nums:
        primes = sieve(n)
        if not primes:
            # No primes to choose from, Ben wins
            winner_count["Ben"] += 1
        else:
            winner = playGame(primes, "Maria", "Ben")
            winner_count[winner] += 1

    if winner_count["Maria"] == winner_count["Ben"]:
        return None
    elif winner_count["Maria"] > winner_count["Ben"]:
        return "Maria"
    else:
        return "Ben"


def sieve(n):
    ''' Returns a list of prime numbers up to n '''
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return [i for i in range(2, n+1) if primes[i]]


def playGame(primes, player1, player2):
    ''' Simulates the game and returns the winner '''

    nums = set(range(1, primes[-1]+1))
    while nums:
        for player in [player1, player2]:
            choices = [p for p in primes if p in nums]
            if not choices:
                return player2 if player == player1 else player1
            chosen = max(choices)
            nums -= set(range(chosen, primes[-1]+1, chosen))

    return player2 if player == player1 else player1
