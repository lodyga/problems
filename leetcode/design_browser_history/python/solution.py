class DoublyLinkedList:
    def __init__(self, url=None, next=None, prev=None) -> None:
        self.url = url
        self.next = next
        self.prev = prev


class BrowserHistory:
    """
    Time complexity:
        constructor: O(1),
        visit: O(1),
        back: O(n),
        forward: O(n)
    Auxiliary space complexity: O(n)
    Tags:
        DS: doubly linked list
        A: iteration
    """

    def __init__(self, homepage) -> None:
        self.active_node = DoublyLinkedList(homepage)

    def visit(self, url) -> None:
        node = self.active_node
        node.next = DoublyLinkedList(url, None, node)
        self.active_node = node.next

    def _cycle(self, steps: int, direction) -> str:
        node = self.active_node

        while steps and getattr(node, direction):
            node = getattr(node, direction)
            steps -= 1

        self.active_node = node
        return node.url

    def back(self, steps: int) -> str:
        return self._cycle(steps, "prev")

    def forward(self, steps: int) -> str:
        return self._cycle(steps, "next")


class DoublyLinkedList:
    def __init__(self, url=None, next=None, prev=None) -> None:
        self.url = url
        self.next = next
        self.prev = prev


class BrowserHistory:
    """
    Time complexity:
        constructor: O(1),
        visit: O(1),
        back: O(n),
        forward: O(n)
    Auxiliary space complexity: O(n)
    Tags:
        DS: doubly linked list
        A: iteration
    """

    def __init__(self, url) -> None:
        self.active_node = DoublyLinkedList(url)

    def visit(self, url) -> None:
        node = self.active_node
        node.next = DoublyLinkedList(url, None, node)
        self.active_node = node.next

    def _cycle(self, steps: int, move) -> str:
        node = self.active_node

        while steps and move(node):
            node = move(node)
            steps -= 1

        self.active_node = node
        return node.url

    def back(self, steps: int) -> str:
        return self._cycle(steps, lambda node: node.prev)

    def forward(self, steps: int) -> str:
        return self._cycle(steps, lambda node: node.next)


browser_history = BrowserHistory("leetcode.com")
browser_history.visit("google.com")
browser_history.visit("facebook.com")
browser_history.visit("youtube.com")
print(browser_history.back(1) == "facebook.com")
print(browser_history.back(1) == "google.com")
print(browser_history.forward(1) == "facebook.com")
browser_history.visit("linkedin.com")
print(browser_history.forward(2) == "linkedin.com")
print(browser_history.back(2) == "google.com")
print(browser_history.back(7) == "leetcode.com")
