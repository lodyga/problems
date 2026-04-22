class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: string
            A: two pointers
        """
        if sentence1 == sentence2:
            return True

        if len(sentence2) > len(sentence1):
            sentence1, sentence2 = sentence2, sentence1

        words1 = sentence1.split()
        words2 = sentence2.split()
        left = 0
        right1 = len(words1) - 1
        right2 = len(words2) - 1

        for word2 in words2:
            if words1[left] == word2:
                left += 1
            else:
                break

        while left <= right2:
            if words1[right1] == words2[right2]:
                right1 -= 1
                right2 -= 1
            else:
                return False

        return True


print(Solution().areSentencesSimilar("My name is Haley", "My Haley") == True)
print(Solution().areSentencesSimilar("of", "A lot of words") == False)
print(Solution().areSentencesSimilar("Eating right now", "Eating") == True)
print(Solution().areSentencesSimilar("H BCp pN LVM RjAe GB oGQDb", "H BCp pN oGQDb") == True)
print(Solution().areSentencesSimilar("A", "a A b A") == True)
