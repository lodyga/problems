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
        suggested_product_list = []

        for letter in word:
            if letter not in node.letters:
                blank = [[]
                         for _ in range(len(word) - len(suggested_product_list))]
                suggested_product_list.extend(blank)
                break

            node = node.letters[letter]
            suggested_product_list.append(node.suggested_products)

        return suggested_product_list


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


class Solution:
    def suggestedProducts(self, products: list[str], search_word: str) -> list[list[str]]:
        """
        Time complexity: O(nlogn + s)
            n: product list length
            s: search word length
        Auxiliary space complexity: O(n)
        Tags: two pointers, sorting
        """
        products.sort()
        left = 0
        right = len(products) - 1
        suggested_product_list = []

        for index, letter in enumerate(search_word):
            while left <= right and (
                len(products[left]) <= index or
                letter != products[left][index]
            ):
                left += 1

            while left <= right and (
                len(products[right]) <= index or
                letter != products[right][index]
            ):
                right -= 1

            product_list = products[left: min(left + 3, right + 1)]
            suggested_product_list.append(product_list)

        return suggested_product_list


print(Solution().suggestedProducts(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse") == [["mobile", "moneypot", "monitor"], ["mobile", "moneypot", "monitor"], ["mouse", "mousepad"], ["mouse", "mousepad"], ["mouse", "mousepad"]])
print(Solution().suggestedProducts(["havana"], "havana") == [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]])
print(Solution().suggestedProducts(["havana"], "tatiana") == [[], [], [], [], [], [], []])
