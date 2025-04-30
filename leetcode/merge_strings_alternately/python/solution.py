class Solution:
    def mergeAlternately(self, word_1: str, word_2:str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        """
        letter_list = []
        index_1 = 0
        index_2 = 0
        
        while index_1 < len(word_1) and index_2 < len(word_2):
            letter_list.append(word_1[index_1])
            index_1 += 1
            letter_list.append(word_2[index_2])
            index_2 += 1
        
        while index_1 < len(word_1):
            letter_list.append(word_1[index_1])
            index_1 += 1
        while index_2 < len(word_2):
            letter_list.append(word_2[index_2])
            index_2 += 1

        return "".join(letter_list)


class Solution:
    def mergeAlternately(self, word_1: str, word_2: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        """
        concatenated_str = ""

        for index in range(max(len(word_1), len(word_2))):
            letter = word_1[index] if index < len(word_1) else ""
            concatenated_str += letter
            letter = word_2[index] if index < len(word_2) else ""
            concatenated_str += letter

        return concatenated_str


print(Solution().mergeAlternately("abc", "pqr") == "apbqcr")
print(Solution().mergeAlternately("ab", "pqrs") == "apbqrs")
print(Solution().mergeAlternately("abcd", "pq") == "apbqcd")