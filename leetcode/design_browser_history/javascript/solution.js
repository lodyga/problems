class DoublyListNode {
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
    * Tags: 
    *     DS: doubly linked list
    *     A: iteration
    */
   constructor(homepage) {
      this.active = new DoublyListNode(homepage);
   };

   visit(url) {
      this.active.next = new DoublyListNode(url, null, this.active);
      this.active = this.active.next;
   };

   back(steps) {
      while (steps && this.active.prev) {
         this.active = this.active.prev;
         steps--;
      }
      return this.active.val
   };

   forward(steps) {
      while (steps && this.active.next) {
         steps--;
         this.active = this.active.next;
      }
      return this.active.val
   };
}


const browserHistory = new BrowserHistory('leetcode.com');
browserHistory.visit('google.com')
browserHistory.visit('facebook.com')
browserHistory.visit('youtube.com')
console.log(browserHistory.back(1) === 'facebook.com')
console.log(browserHistory.back(1) === 'google.com')
console.log(browserHistory.forward(1) === 'facebook.com')
browserHistory.visit('linkedin.com')
console.log(browserHistory.forward(2) === 'linkedin.com')
console.log(browserHistory.back(2) === 'google.com')
console.log(browserHistory.back(7) === 'leetcode.com')
