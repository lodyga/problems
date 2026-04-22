class Solution:
    """
    Time complexity: O(n):
        n: char count
    Auxiliary space complexity: O(n)
    Tags:
        DS: list
        A: iteration
    """

    def encode(self, words: list[str]) -> str:
        res = []

        for word in words:
            res.append(f"${(len(word))}\r\n")
            res.append(f"{word}\r\n")

        return "".join(res)

    def decode(self, text: str) -> list[str]:
        res = []

        for idx, item in enumerate(text.split("\r\n")):
            if idx % 2:
                res.append(item)

        return res


class Solution:
    """
    Time complexity: O(n):
        n: char count
    Auxiliary space complexity: O(n)
    Tags:
        DS: list
        A: iteration
    """

    def encode(self, words: list[str]) -> str:
        res = []

        for word in words:
            res.append(str(len(word)))
            res.append("#")
            res.append(word)
        return "".join(res)

    def decode(self, text: str) -> list[str]:
        res = []
        index = 0

        while index < len(text):
            word_length = 0
            while text[index] != "#":
                word_length = word_length * 10 + int(text[index])
                index += 1

            index += 1
            res.append(text[index: index + word_length])
            index += word_length

        return res


print(Solution().encode(["code", "site", "who", "you"]) == "$4\r\ncode\r\n$4\r\nsite\r\n$3\r\nwho\r\n$3\r\nyou\r\n")
print(Solution().decode(Solution().encode(["code", "site", "who", "you"])) == ["code", "site", "who", "you"])
print(Solution().decode(Solution().encode([""])) == [""])
print(Solution().decode(Solution().encode(["1,23","45,6","7,8,9"])) == ["1,23","45,6","7,8,9"])
