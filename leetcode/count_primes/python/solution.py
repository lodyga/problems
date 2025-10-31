# primes
# 2, 3, 5, 7, 11, 13, 17, 19, 23


class Solution:
    def countPrimes(self, n: int) -> int:
        """
        Time complexity: O(n*sqrt(n))
        Auxiliary space complexity: O(n)
        Tags: tle, iteration
        """
        if n < 3:
            return 0
        
        primes = [2]
        for prime_candidate in range(3, n, 2):
            is_add = True
            
            for prime in primes:
                if prime_candidate % prime == 0:
                    is_add = False
                    break
                if prime_candidate < prime * 2:
                    break
            
            if is_add:
                primes.append(prime_candidate)
            
            prime_candidate += 1
        
        return len(primes)


class Solution:
    def countPrimes(self, n: int) -> int:
        """
        Time complexity: O(n log log n)
        Auxiliary space complexity: O(n)
        Tags: sieve of eratosthenes, primes
        """
        if n < 3:
            return 0
        if n == 3:
            return 1

        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        for index in range(2, int(n**0.5) + 1):
            if is_prime[index]:
                # for i2 in range(index**2, n + 1, index):
                #     is_prime[i2] = False
                is_prime[index**2: : index] = [False] * len(is_prime[index**2: : index])
        
        return sum(is_prime[:n])


print(Solution().countPrimes(10), 4)
print(Solution().countPrimes(20), 8)
print(Solution().countPrimes(0), 0)
print(Solution().countPrimes(1), 0)
print(Solution().countPrimes(2), 0)
print(Solution().countPrimes(3), 1)
print(Solution().countPrimes(19), 7)
print(Solution().countPrimes(499979), 41537)