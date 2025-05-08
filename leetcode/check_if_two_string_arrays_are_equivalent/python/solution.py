class Solution:
    def arrayStringsAreEqual(self, word_list1: list[str], word_list2: list[str]) -> bool:
        """
        Time complexity: O(m+n)
        Auxiliary space complexity: O(1)
        Tags: generator
        """
        def gnerate_letter(word_list):
            for word in word_list:
                for letter in word:
                    yield letter

        letter1, letter2 = 0, 0
        is_end1, is_end2 = False, False

        generated_letters1 = gnerate_letter(word_list1)
        generated_letters2 = gnerate_letter(word_list2)
        
        while True:
            try:
                letter1 = next(generated_letters1)
            except:
                is_end1 = True
            try:
                letter2 = next(generated_letters2)
            except:
                is_end2 = True

            if is_end1 or is_end2:
                return is_end1 == is_end2
            
            if letter1 != letter2:
                return False


class Solution:
    def arrayStringsAreEqual(self, word_list1: list[str], word_list2: list[str]) -> bool:
        """
        Time complexity: O(m+n)
        Auxiliary space complexity: O(1)
        Tags: two pointers
        """
        def get_letter_or_end(letter, word, word_list, is_end):
            letter += 1
            if letter == len(word_list[word]):
                word += 1
                letter = 0
                if word == len(word_list):
                    return (None, None, True)

            return (letter, word, is_end)

        word1, word2 = 0, 0
        letter1, letter2 = 0, 0
        is_end1, is_end2 = False, False

        while True:
            if word_list1[word1][letter1] != word_list2[word2][letter2]:
                return False

            letter1, word1, is_end1 = get_letter_or_end(letter1, word1, word_list1, is_end1)
            letter2, word2, is_end2 = get_letter_or_end(letter2, word2, word_list2, is_end2)

            if is_end1 or is_end2:
                return is_end1 == is_end2


class Solution:
    def arrayStringsAreEqual(self, word_list1: list[str], word_list2: list[str]) -> bool:
        """
        Time complexity: O(m+n)
        Auxiliary space complexity: O(m+n)
        Tags: build-in function
        """
        return "".join(word_list1) == "".join(word_list2)


print(Solution().arrayStringsAreEqual(["ab", "c"], ["a", "bc"]), True)
print(Solution().arrayStringsAreEqual(["a", "cb"], ["ab", "c"]), False)
print(Solution().arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]), True)
print(Solution().arrayStringsAreEqual(["abc", "d", "defg"], ["abcddef"]), False)