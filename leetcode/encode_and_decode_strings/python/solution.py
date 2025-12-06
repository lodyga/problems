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
        encoded = []
        for word in words:
            encoded.append(str(len(word)))
            encoded.append("#")
            encoded.append(word)
        return "".join(encoded)

    def decode(self, text: str) -> list[str]:
        words = []
        index = 0

        while index < len(text):
            word_length = 0
            while text[index] != "#":
                word_length = word_length * 10 + int(text[index])
                index += 1
        
            index += 1
            words.append(text[index: index + word_length])
            index += word_length

        return words


print(Solution().encode(["code", "site", "love", "you"]) == "4#code4#site4#love3#you")
print(Solution().decode(Solution().encode(["code", "site", "love", "you"])) == ["code", "site", "love", "you"])
print(Solution().decode(Solution().encode([""])) == [""])
print(Solution().decode(Solution().encode(["1,23","45,6","7,8,9"])) == ["1,23","45,6","7,8,9"])
