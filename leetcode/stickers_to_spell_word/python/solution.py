class Solution:
    def minStickers(self, stickers: list[str], target: str) -> int:
        """
        Time complexity: O(n2^n)
            n: target length
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map, array, list, tuple
            A: top-down
        """
        target_letter_freq = [0] * 26
        stickers_letter_freq = []
        memo = {tuple([0]*26): 0}

        for letter in target:
            idx = ord(letter) - ord("a")
            target_letter_freq[idx] += 1

        for sticker in stickers:
            sticker_letter_freq = [0] * 26
            is_letter = False

            for letter in sticker:
                idx = ord(letter) - ord("a")

                if target_letter_freq[idx]:
                    is_letter = True

                    sticker_letter_freq[idx] += 1

            if is_letter:
                stickers_letter_freq.append(sticker_letter_freq)

        def dfs(taregt_letter_freq):
            if taregt_letter_freq in memo:
                return memo[taregt_letter_freq]

            res = float("inf")

            for sticker_letter_freq in stickers_letter_freq:
                for idx in range(26):
                    if taregt_letter_freq[idx]:
                        skip_word = sticker_letter_freq[idx] == 0
                        break

                if skip_word:
                    continue

                target_letter_freq_list = list(taregt_letter_freq)

                for idx in range(26):
                    if sticker_letter_freq[idx]:
                        target_letter_freq_list[idx] -= sticker_letter_freq[idx]
                        target_letter_freq_list[idx] = max(
                            0, target_letter_freq_list[idx])

                res = min(res, 1 + dfs(tuple(target_letter_freq_list)))

            memo[taregt_letter_freq] = res
            return res

        res = dfs(tuple(target_letter_freq))
        return -1 if res == float("inf") else res


print(Solution().minStickers(["with", "example", "science"], "thehat") == 3)
print(Solution().minStickers(["notice", "possible"], "basicbasic") == -1)
print(Solution().minStickers(["fly", "me", "charge", "mind", "bottom"], "centorder") == 4)
print(Solution().minStickers(["control", "heart", "interest", "stream", "sentence", "soil", "wonder", "them", "month", "slip", "table", "miss", "boat", "speak", "figure", "no", "perhaps", "twenty", "throw", "rich", "capital", "save", "method", "store", "meant", "life", "oil", "string", "song", "food", "am", "who", "fat", "if", "put", "path", "come", "grow", "box", "great", "word", "object", "stead", "common", "fresh", "the", "operate", "where", "road", "mean"], "stoodcrease") == 3)
