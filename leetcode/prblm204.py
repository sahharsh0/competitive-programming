#Given an integer n, return the number of prime numbers that are strictly less than n.
class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        size = n // 2
        is_prime = [1] * size
        is_prime[0] = 0
        for i in range(3, int(n**0.5) + 1, 2):
            if is_prime[i // 2]:
                for j in range(i * i, n, 2 * i):
                    is_prime[j // 2] = 0

        return sum(is_prime) + 1
print(Solution().countPrimes(30)) 