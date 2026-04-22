class DSU:
    def __init__(self, n, sentence) -> None:
        self.size = [1] * n
        self.parent = list(range(n))
        self.word1_set = set(sentence)
        self.word_index = {}
        self.index = 0

    def _get_index(self, word):
        if word not in self.word_index:
            self.word_index[word] = self.index
            self.index += 1

        return self.word_index[word]

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]

        return u

    def union(self, word1, word2):
        u = self._get_index(word1)
        v = self._get_index(word2)
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return
        elif word1 in self.word1_set:
            pass
        elif (
            self.size[pv] > self.size[pu] or
            word2 in self.word1_set
        ):
            pu, pv = pv, pu

        self.size[pu] += self.size[pv]
        self.parent[pv] = self.parent[pu]
        return


class Solution:
    def areSentencesSimilarTwo(self, sentence1: list[str], sentence2: list[str], similarPairs: list[list[str]]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map, list, string
            A: DSU
            Model: graph
        """
        if not len(sentence1) == len(sentence2):
            return False

        dsu = DSU(len(similarPairs)*2, sentence1)

        for (word1, word2) in similarPairs:
            dsu.union(word1, word2)

        for (word1, word2) in zip(sentence1, sentence2):
            if word1 == word2:
                continue
            elif (
                word1 not in dsu.word_index or
                word2 not in dsu.word_index
            ):
                return False

            i1 = dsu.word_index[word1]
            i2 = dsu.word_index[word2]

            if dsu.parent[i1] != dsu.parent[dsu.parent[i2]]:
                return False

        return True


print(Solution().areSentencesSimilarTwo(["great", "acting", "skills"], ["fine", "drama", "talent"], [["great", "good"], ["fine", "good"], ["drama", "acting"], ["skills", "talent"]]) == True)
print(Solution().areSentencesSimilarTwo(["I", "love", "leetcode"], ["I", "love", "onepiece"], [["manga", "onepiece"], ["platform", "anime"], ["leetcode", "platform"], ["anime", "manga"]]) == True)
print(Solution().areSentencesSimilarTwo(["I", "love", "leetcode"], ["I", "love", "onepiece"], [["manga", "hunterXhunter"], ["platform", "anime"], ["leetcode", "platform"], ["anime", "manga"]]) == False)
