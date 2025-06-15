class ListNode {
   constructor(val = null, next = null, prev = null) {
      this.val = val;
      this.next = next;
      this.prev = prev;
   }
}


class BrowserHistory {
   /**
    * Time complexity:
    *     constructor: O(1),
    *     visit: O(1),
    *     back: O(n),
    *     forward: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: linked list
    */
   constructor(homepage) {
      this.home = new ListNode(homepage);
      this.node = this.home;
   };

   visit(url) {
      this.node.next = new ListNode(url, null, this.node);
      this.node = this.node.next;
   };

   back(steps) {
      while (steps && this.node.prev) {
         steps--;
         this.node = this.node.prev;
      }
      return this.node.val
   };

   forward(steps) {
      while (steps && this.node.next) {
         steps--;
         this.node = this.node.next;
      }
      return this.node.val
   };
}


const browserHistory = new BrowserHistory('leetcode.com');
browserHistory.visit('google.com');  // You are in 'leetcode.com'. Visit 'google.com'
browserHistory.visit('facebook.com');  // You are in 'google.com'. Visit 'facebook.com'
browserHistory.visit('youtube.com');  // You are in 'facebook.com'. Visit 'youtube.com'
console.log(browserHistory.back(1));  // You are in 'youtube.com', move back to 'facebook.com' return 'facebook.com'
console.log(browserHistory.back(1));  // You are in 'facebook.com', move back to 'google.com' return 'google.com'
console.log(browserHistory.forward(1));  // You are in 'google.com', move forward to 'facebook.com' return 'facebook.com'
browserHistory.visit('linkedin.com');  // You are in 'facebook.com'. Visit 'linkedin.com'
console.log(browserHistory.forward(2));  // You are in 'linkedin.com', you cannot move forward any steps.
console.log(browserHistory.back(2));  // You are in 'linkedin.com', move back two steps to 'facebook.com' then to 'google.com'. return 'google.com'
console.log(browserHistory.back(7));  // You are in 'google.com', you can move back only one step to 'leetcode.com'. return 'leetcode.com'