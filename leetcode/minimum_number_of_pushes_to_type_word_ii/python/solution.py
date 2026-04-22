class Solution:
    def minimumPushes(self, word: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list, array
            A: bucket sort
        """
        pushes = 0
        letter_freq = [0] * 26

        for letter in word:
            idx = ord(letter) - ord("a")
            letter_freq[idx] += 1

        # index + 1 -> frequency; value -> letter counter
        freq_bucket = [0] * max(letter_freq)

        for freq in letter_freq:
            if freq:
                freq_bucket[freq - 1] += 1

        # 8 letters per layer
        layer_letters = 0
        # pushes in current layer
        layer_pushes = 1

        for idx in range(len(freq_bucket) - 1, -1, -1):
            # (counter, freq) => (how many letters, frequency of current letter)
            counter = freq_bucket[idx]

            if counter:
                freq = idx + 1

                while layer_letters + counter >= 8:
                    diff = 8 - layer_letters
                    pushes += diff * freq * layer_pushes
                    layer_pushes += 1
                    counter -= diff
                    layer_letters = (layer_letters + diff) % 8

                pushes += counter * freq * layer_pushes
                layer_letters = layer_letters + counter

        return pushes


print(Solution().minimumPushes("abcde") == 5)
print(Solution().minimumPushes("xyzxyzxyzxyz") == 12)
print(Solution().minimumPushes("aabbccddeeffgghhiiiiii") == 24)
print(Solution().minimumPushes("hiknogatpyjzcdbe") == 24)
