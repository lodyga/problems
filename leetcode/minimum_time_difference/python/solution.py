class Solution:
    def findMinDifference(self, time_points: list[str]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: sorting
        """
        times = [(int(h1) * 10 + int(h2), int(m1) * 10 + int(m2))
                 for h1, h2, _, m1, m2 in time_points]
        times.sort()
        h0, m0 = times[0]
        times.append((24 + h0, m0))
        res = 24 * 60

        for index in range(len(times) - 1):
            h1, m1 = times[index]
            h2, m2 = times[index + 1]
            res = min(res, (h2 - h1) * 60 + (m2 - m1))

            if res == 0:
                return 0

        return res


class Solution:
    def findMinDifference(self, time_points: list[str]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: sorting
        """
        times = [((int(h1) * 10 + int(h2)) * 60 + int(m1) * 10 + int(m2))
                 for h1, h2, _, m1, m2 in time_points]
        times.sort()
        times.append(times[0] + 24 * 60)
        res = 24 * 60

        for index in range(len(times) - 1):
            res = min(res, times[index + 1] - times[index])

            if res == 0:
                return 0

        return res


print(Solution().findMinDifference(["23:59", "00:00"]) == 1)
print(Solution().findMinDifference(["00:00", "23:59", "00:00"]) == 0)
print(Solution().findMinDifference(["02:39", "10:26", "21:43"]) == 296)
print(Solution().findMinDifference(["00:01", "01:59"]) == 118)
