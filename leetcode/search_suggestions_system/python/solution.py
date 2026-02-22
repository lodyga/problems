class Solution:
    def suggestedProducts(self, products: list[str], search_word: str) -> list[list[str]]:
        """
        Time complexity: O(nlogn + n*s2)
            n: product list length
            s: search word length
        Auxiliary space complexity: O(n)
        Tags:
            A: sorting
        """
        products.sort()
        prefix = ""
        res = []
        start = 0

        for letter in search_word:
            prefix = prefix + letter
            res_part = []
            is_new_start = False

            for index in range(start, len(products)):
                word = products[index]

                if word.startswith(prefix):
                    res_part.append(word)

                    if is_new_start == False:
                        start = index
                        is_new_start = True

                    if len(res_part) == 3:
                        break

            res.append(res_part)

        return res


class Solution:
    def suggestedProducts(self, products: list[str], search_word: str) -> list[list[str]]:
        """
        Time complexity: O(nlogn)
            n: product list length
            s: search word length
        Auxiliary space complexity: O(n)
        Tags:
            A: two pointers, sorting
        """
        products.sort()
        res = []
        left = 0
        right = len(products) - 1

        for index in range(len(search_word)):
            search_letter = search_word[index]

            while (
                left <= right and
                (
                    len(products[left]) <= index or
                    search_letter != products[left][index]
                )
            ):
                left += 1
            while (
                left <= right and
                (
                    len(products[right]) <= index or
                    search_letter != products[right][index]
                )
            ):
                right -= 1

            res.append(products[left: min(left + 3, right + 1)])

        return res


class TrieNode:
    def __init__(self) -> None:
        self.letters = {}
        self.is_word = False
        self.suggested_products = []


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def add(self, word: str) -> None:
        node = self.root

        for letter in word:
            if letter not in node.letters:
                node.letters[letter] = TrieNode()

            node = node.letters[letter]
            
            if len(node.suggested_products) < 3:
                node.suggested_products.append(word)

        node.is_word = True

    def get_suggestions(self, word: str) -> list[list[str]]:
        node = self.root
        res = []

        for letter in word:
            if letter not in node.letters:
                blank = [[] for _ in range(len(word) - len(res))]
                res.extend(blank)
                break

            node = node.letters[letter]
            res.append(node.suggested_products)

        return res


class Solution:
    def suggestedProducts(self, products: list[str], search_word: str) -> list[list[str]]:
        """
        Time complexity: O(n*l)
            n: product list length
            l: avg product length
        Auxiliary space complexity: O(n*l)
        Tags: trie
        """
        products.sort()
        trie = Trie()
        for product in products:
            trie.add(product)

        return trie.get_suggestions(search_word)


print(Solution().suggestedProducts(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse") == [["mobile", "moneypot", "monitor"], ["mobile", "moneypot", "monitor"], ["mouse", "mousepad"], ["mouse", "mousepad"], ["mouse", "mousepad"]])
print(Solution().suggestedProducts(["havana"], "havana") == [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]])
print(Solution().suggestedProducts(["havana"], "tatiana") == [[], [], [], [], [], [], []])
