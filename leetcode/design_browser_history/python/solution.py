class DoublyListNode:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
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

    def __init__(self, homepage: str):
        self.active = DoublyListNode(homepage)

    def visit(self, url: str) -> None:
        self.active.next = DoublyListNode(url, None, self.active)
        self.active = self.active.next

    def back(self, steps: int) -> str:
        while steps and self.active.prev:
            self.active = self.active.prev
            steps -= 1
        return self.active.val

    def forward(self, steps: int) -> str:
        while steps and self.active.next:
            self.active = self.active.next
            steps -= 1
        return self.active.val


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
