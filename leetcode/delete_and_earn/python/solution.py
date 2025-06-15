class Solution:
    def deleteAndEarn(self, numbers: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up
        """
        number_frequency = {}
        for number in numbers:
            number_frequency[number] = number_frequency.get(number, 0) + 1

        unique_sorted_numbers = sorted(set(numbers))
        cache = [0] * len(unique_sorted_numbers)

        for index, number in enumerate(unique_sorted_numbers):
            cache[index] = number * number_frequency[number]

            if index == 0:
                continue
            elif unique_sorted_numbers[index - 1] + 1 == number:
                cache[index] = max(
                    cache[index - 1],
                    cache[index] + (cache[index - 2] if index != 1 else 0)
                )
            else:
                cache[index] += cache[index - 1]

        return cache[-1]


class Solution:
    def deleteAndEarn(self, numbers: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up
        cache optimized
        """
        number_frequency = {}
        for number in numbers:
            number_frequency[number] = number_frequency.get(number, 0) + 1

        unique_sorted_numbers = sorted(set(numbers))
        
        for index, number in enumerate(unique_sorted_numbers):
            current_cache = number * number_frequency[number]

            if index == 0:
                cache = [0, current_cache]
                continue
            elif unique_sorted_numbers[index - 1] + 1 == number:
                current_cache = max(
                    current_cache + (cache[0] if index != 1 else 0),
                    cache[1]
                )
            else:
                current_cache += cache[1]
            
            cache = [cache[1], current_cache]

        return cache[-1]


print(Solution().deleteAndEarn([1]) == 1)
print(Solution().deleteAndEarn([2, 3]) == 3)
print(Solution().deleteAndEarn([2, 4]) == 6)
print(Solution().deleteAndEarn([3, 4, 2]) == 6)
print(Solution().deleteAndEarn([2, 2, 3, 3, 3, 4]) == 9)
print(Solution().deleteAndEarn([8, 10, 4, 9, 1, 3, 5, 9, 4, 10]) == 37)
print(Solution().deleteAndEarn([1, 1, 1, 2, 4, 5, 5, 5, 6]) == 18)
print(Solution().deleteAndEarn([1, 6, 3, 3, 8, 4, 8, 10, 1, 3]) == 43)
print(Solution().deleteAndEarn([1, 1, 1]) == 3)
print(Solution().deleteAndEarn([12, 32, 93, 17, 100, 72, 40, 71, 37, 92, 58, 34, 29, 78, 11, 84, 77, 90, 92, 35, 12, 5, 27, 92, 91, 23, 65, 91, 85, 14, 42, 28, 80, 85, 38, 71, 62, 82, 66, 3, 33, 33, 55, 60, 48, 78, 63, 11, 20, 51, 78, 42, 37, 21, 100, 13, 60, 57, 91, 53, 49, 15, 45, 19, 51, 2, 96, 22, 32, 2, 46, 62, 58, 11, 29, 6, 74, 38, 70, 97, 4, 22, 76, 19, 1, 90, 63, 55, 64, 44, 90, 51, 36, 16, 65, 95, 64, 59, 53, 93]) == 3451)


class Solution:
    def deleteAndEarn(self, numbers: list[int]) -> int:
        """
        O(n), O(n)
        dp, top-down with memoization as list
        """
        counter = {}
        for number in numbers:
            counter[number] = counter.get(number, 0) + 1

        sorted_numbers = sorted(set(numbers))
        memo = [None] * (len(sorted_numbers) + 2)
        memo[-1] = memo[-2] = 0

        def dfs(index: int) -> int:
            if memo[index] is not None:
                return memo[index]
            
            number = sorted_numbers[index]
            val = number * counter[number]

            if (index + 1 < len(sorted_numbers) and 
                    sorted_numbers[index] + 1 != sorted_numbers[index + 1]):
                val += dfs(index + 1)
            else:
                val += dfs(index + 2)
            
            memo[index] = max(val, dfs(index + 1))
            return memo[index]

        return dfs(0)


class Solution:
    def deleteAndEarn(self, numbers: list[int]) -> int:
        """
        O(n), O(n)
        dp, top-down with memoization as hash map
        """
        counter = {}
        for number in numbers:
            counter[number] = counter.get(number, 0) + 1

        sorted_numbers = sorted(set(numbers))
        memo = {
            len(sorted_numbers): 0, 
            len(sorted_numbers) + 1: 0
        }

        def dfs(index: int) -> int:
            if index in memo:
                return memo[index]
            
            number = sorted_numbers[index]
            val = number * counter[number]

            if (index + 1 < len(sorted_numbers) and 
                    sorted_numbers[index] + 1 != sorted_numbers[index + 1]):
                val += dfs(index + 1)
            else:
                val += dfs(index + 2)
            
            memo[index] = max(val, dfs(index + 1))
            return memo[index]

        return dfs(0)


class Solution:
    def deleteAndEarn(self, numbers: list[int]) -> int:
        """
        O(2^n), O(n)
        brute force, tle
        """
        counter = {}
        for number in numbers:
            counter[number] = counter.get(number, 0) + 1

        sorted_numbers = sorted(set(numbers))

        def dfs(index: int) -> int:
            if index >= len(sorted_numbers):
                return 0
            
            number = sorted_numbers[index]
            val = number * counter[number]

            if (index + 1 < len(sorted_numbers) and 
                    sorted_numbers[index] + 1 != sorted_numbers[index + 1]):
                val += dfs(index + 1)
            else:
                val += dfs(index + 2)
            
            return max(val, dfs(index + 1))

        return dfs(0)
