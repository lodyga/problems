class Solution:
    def alienOrder(self, words: list[str]) -> str:
        """
        Time complexity: O(n)
            n: unique letter set length
        Auxiliary space complexity: O(n)
        Tags: dfs, recursion, graph, topological sort
        """
        letter_order_map = {}  # {letter: set(following letters)}

        for index in range(len(words) - 1):
            word1 = words[index]
            word2 = words[index + 1]

            index2 = 0
            while True:
                # if the first word is seconds prefix
                if len(word1) == index2 and len(word2) > index2:
                    break
                # if the second word is firsts prefix
                elif len(word2) == index2 and len(word1) > index2:
                    return ""
                letter1 = word1[index2]
                letter2 = word2[index2]
                
                if letter1 == letter2:
                    index2 += 1
                    continue
                
                if letter1 not in letter_order_map:  
                    letter_order_map[letter1] = set()
                letter_order_map[letter1].add(letter2)
                break
        
        visited = set()
        path = set()
        letter_order = []
        
        def dfs(letter):
            # detect cycle
            if letter in path:
                return False
            # if already visited
            elif letter in visited:
                return True

            path.add(letter)

            if letter in letter_order_map:
                for preq_letter in letter_order_map[letter]:
                    if dfs(preq_letter) == False:
                        return False

            letter_order.append(letter)
            path.remove(letter)
            visited.add(letter)


        for letter in letter_order_map:
            if dfs(letter) == False:
                return ""

        return "".join(reversed(letter_order))


class Solution:
    def alienOrder(self, words: list[str]) -> str:
        """
        Time complexity: O(n)
            n: unique letter length
        Auxiliary space complexity: O(n)
        Tags: dfs, recursion, graph, topological sort
        """
        # adjacency list, {parent: set(child1, child2), }, child comes after parent
        adj = {chr: set() for word in words for chr in word}

        for index in range(len(words) - 1):
            word1 = words[index]
            word2 = words[index + 1]
            min_word_len = min(len(word1), len(word2))
            # if same prefix and first word is longer => invalid
            if (
                len(word1) > len(word2) and
                word1[:min_word_len] == word2[:min_word_len]
            ):
                return ""

            # build adjacency list
            for ind2 in range(min_word_len):
                if word1[ind2] != word2[ind2]:
                    adj[word1[ind2]].add(word2[ind2])
                    break

        # None: not visited, False: visited, True: (visited and) in the current path => cycle
        visited = {}
        lex_order = []

        def dfs(char):
            if char in visited:
                return visited[char]

            # mark char as in current path
            visited[char] = True

            for child in adj[char]:
                if dfs(child):
                    # cycle detected
                    return True

            visited[char] = False
            # mark char as visited
            lex_order.append(char)

        for char in adj:
            if dfs(char):
                return ""

        return "".join(reversed(lex_order))


print(Solution().alienOrder(["z", "x"]) == "zx")
print(Solution().alienOrder(["z", "o", "z"]) == "")
print(Solution().alienOrder(["a", "ab", "bc", "c"]) == "abc")
print(Solution().alienOrder(["wrt","wrf","er","ett","rftt"]) == "wertf")
print(Solution().alienOrder(["hrn", "hrf", "er", "enn", "rfnn"]) == "hernf")