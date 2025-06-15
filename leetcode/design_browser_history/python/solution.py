class ListNode:
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
    Tags: linked list
    """

    def __init__(self, homepage: str):
        self.home = ListNode(homepage)
        self.node = self.home

    def visit(self, url: str) -> None:
        self.node.next = ListNode(url, None, self.node)
        self.node = self.node.next

    def back(self, steps: int) -> str:
        while steps and self.node.prev:
            steps -= 1
            self.node = self.node.prev
        
        return self.node.val

    def forward(self, steps: int) -> str:
        while steps and self.node.next:
            steps -= 1
            self.node = self.node.next
        
        return self.node.val


browser_history = BrowserHistory("leetcode.com")
browser_history.visit("google.com")  # You are in "leetcode.com". Visit "google.com"
browser_history.visit("facebook.com")  # You are in "google.com". Visit "facebook.com"
browser_history.visit("youtube.com")  # You are in "facebook.com". Visit "youtube.com"
print(browser_history.back(1))  # You are in "youtube.com", move back to "facebook.com" return "facebook.com"
print(browser_history.back(1))  # You are in "facebook.com", move back to "google.com" return "google.com"
print(browser_history.forward(1))  # You are in "google.com", move forward to "facebook.com" return "facebook.com"
browser_history.visit("linkedin.com")  # You are in "facebook.com". Visit "linkedin.com"
print(browser_history.forward(2))  # You are in "linkedin.com", you cannot move forward any steps.
print(browser_history.back(2))  # You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
print(browser_history.back(7))  # You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"