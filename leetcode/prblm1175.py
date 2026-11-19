'''1175. Prime Arrangements
Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)
(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)
Since the answer may be large, return the answer modulo 10^9 + 7.'''
class Solution(object):
    def numPrimeArrangements(self, n):
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True
        prime_count = sum(1 for i in range(1, n + 1) if is_prime(i))
        non_prime_count = n - prime_count
        mod = 10**9 + 7
        def factorial(num):
            result = 1
            for i in range(2, num + 1):
                result = (result * i) % mod
            return result
        return (factorial(prime_count) * factorial(non_prime_count)) % mod
print(Solution().numPrimeArrangements(5))