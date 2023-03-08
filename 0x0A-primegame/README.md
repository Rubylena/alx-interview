# Prime Game
Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.

Prototype: def isWinner(x, nums)
where x is the number of rounds and nums is an array of n
Return: name of the player that won the most rounds
If the winner cannot be determined, return None
You can assume n and x will not be larger than 10000
You cannot import any packages in this task
Example:

x = 3, nums = [4, 5, 1]
First round: 4

Maria picks 2 and removes 2, 4, leaving 1, 3
Ben picks 3 and removes 3, leaving 1
Ben wins because there are no prime numbers left for Maria to choose
Second round: 5

Maria picks 2 and removes 2, 4, leaving 1, 3, 5
Ben picks 3 and removes 3, leaving 1, 5
Maria picks 5 and removes 5, leaving 1
Maria wins because there are no prime numbers left for Ben to choose
Third round: 1

Ben wins because there are no prime numbers for Maria to choose
Result: Ben has the most wins

Explanation:
To solve this problem, we can use the Sieve of Eratosthenes algorithm to generate a list of prime numbers up to n for each round. Then, we can simulate the game by having the players take turns choosing prime numbers and removing their multiples from the list. We can keep track of which player wins each round and return the player that wins the most rounds.

The isWinner function takes the number of rounds x and an array of integers nums as input, where each integer represents the upper limit of the consecutive set of integers for a round. The function first initializes a dictionary winner_count to keep track of how many rounds each player wins. It then loops through each integer n in nums, generates a list of prime numbers up to n using the sieve function, and simulates the game using the playGame function. If there are no prime numbers to choose from, Ben wins by default.

The sieve function uses the Sieve of Eratosthenes algorithm to generate a list of prime numbers up to n. It returns a list of all the prime numbers in that range.

The playGame function takes a list of prime numbers primes and the names of two players player1 and player2 as input. It simulates the game by first initializing a set nums of all the integers from 1 up to and including the largest prime number in primes. It then alternates between the two players, allowing each player to choose a prime number from primes that is still in nums and removing its multiples from nums. The function returns the name of the player that cannot make a move, i.e., the player that is left with no prime numbers to choose from.

Finally, the isWinner function compares the number of rounds each player wins in winner_count and