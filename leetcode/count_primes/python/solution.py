class Solution:
    def countPrimes(self, n: int) -> int:
        """
        Time complexity: O(n*sqrt(n))
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        def is_prime(num):
            for divider in range(2, int(num**0.5) + 1):
                if num % divider == 0:
                    return False
            return True

        if n < 3:
            return 0

        counter = 1

        for num in range(3, n, 2):
            counter += is_prime(num)

        return counter


class Solution:
    def countPrimes(self, n: int) -> int:
        """
        Time complexity: O(n*log(log n))
        Auxiliary space complexity: O(n)
        Tags: 
            A: sieve of eratosthenes, primes
        """
        if n < 3:
            return 0
        if n == 3:
            return 1

        is_prime = [True] * (n + 1)
        is_prime[0] = False
        is_prime[1] = False

        for num in range(2, int(n**0.5) + 1):
            if is_prime[num]:
                # for multi in range(num*2, n + 1, num):
                #     is_prime[multi] = False
                is_prime[num*2:: num] = [False] * len(is_prime[num*2:: num])

        is_prime.pop()
        return sum(is_prime)


print(Solution().countPrimes(10) == 4)
print(Solution().countPrimes(20) == 8)
print(Solution().countPrimes(0) == 0)
print(Solution().countPrimes(1) == 0)
print(Solution().countPrimes(2) == 0)
print(Solution().countPrimes(3) == 1)
print(Solution().countPrimes(19) == 7)
print(Solution().countPrimes(499979) == 41537)
