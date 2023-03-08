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
The script defines two functions, isPrime(n) and isWinner(x, nums).

isPrime(n) is a function that returns a list of prime numbers between 1 and n. The function uses the sieve of Eratosthenes algorithm to find prime numbers. The function creates a list called sieve with n+1 elements, and sets each element to True. The loop iterates from 2 to n, and for each number num, if sieve[num] is True, the number is added to the primeNums list, and all multiples of num up to n are marked as composite (not prime) by setting their corresponding element in the sieve list to False. Finally, the function returns the list of prime numbers primeNums.

isWinner(x, nums) is a function that determines the winner of a game based on a list of integers nums and a parameter x. The game involves finding prime numbers in each integer in the nums list up to the index x-1, and assigning a point to the player based on whether the number of prime numbers in the integer is odd or even. If the number of prime numbers is odd, the point goes to player Maria, otherwise it goes to player Ben. The function returns the name of the winner (either "Maria" or "Ben"), or None if the inputs are invalid.

The function first checks if the input parameters are None, if x is equal to 0, or if nums is an empty list. If any of these conditions are true, the function returns None.

The function then initializes variables mariaCount and benCount to 0. The function then iterates through the first x elements of the nums list using a for loop. For each element in nums, the function calls isPrime(n) to get the list of prime numbers in that element, and determines if the number of prime numbers in that element is odd or even. If the number of prime numbers is odd, mariaCount is incremented, otherwise benCount is incremented.

Finally, the function compares the mariaCount and benCount variables, and returns the name of the winner based on who has the higher count, or None if the counts are equal.