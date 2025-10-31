class Solution:
    def primeSubOperation(self, numbers: list[int]) -> bool:
        """
        Time complexity: O(nlogm + n*sqrt(m))
            n: number count
            m: max number
        Auxiliary space complexity: O(1)
        Tags: binary search
        """
        # primes = [2, 3, 5, 7, 11, 13, 17, 23]
        # Generate primes.
        is_prime = [True] * (max(numbers) + 1)
        is_prime[0] = is_prime[1] = False
        for index in range(2, int(max(numbers)**0.5) + 1):
            if is_prime[index]:
                for i2 in range(index*index, max(numbers) + 1, index):
                    is_prime[i2] = False
        primes = [index for index, b in enumerate(is_prime) if b]

        # Make array strictly increasing. 
        for index in reversed(range(len(numbers) - 1)):
            if numbers[index] < numbers[index + 1]:
                continue
            
            diff = numbers[index] - numbers[index + 1] + 1
            left = 0
            right = len(primes) - 1
            min_diff = None
                
            while left <= right:
                middle = (left + right) >> 1
                middle_number = primes[middle]

                # subtract as much as possilbe
                if diff > middle_number:
                    left = middle + 1
                else:
                    right = middle - 1
                    min_diff = middle_number
            
            if min_diff is None:
                return False
            numbers[index] -= min_diff
            if numbers[index] >= numbers[index + 1]:
                return False            
            if numbers[index] <= 0:
                return False
        
        return True


print(Solution().primeSubOperation([6, 8, 11, 12]) == True)
print(Solution().primeSubOperation([4, 9, 6, 10]) == True)
print(Solution().primeSubOperation([5, 8, 3]) == False)
print(Solution().primeSubOperation([2, 2]) == False)
print(Solution().primeSubOperation([8, 19, 3, 4, 9]) == True)
print(Solution().primeSubOperation([18, 12, 14, 6]) == False)
print(Solution().primeSubOperation([4, 18, 10, 16, 3]) == False)
print(Solution().primeSubOperation([16, 8, 4]) == False)
print(Solution().primeSubOperation([6, 16, 2]) == False)