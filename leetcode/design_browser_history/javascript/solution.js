class DoublyLinkedNode {
   constructor(url = null, next = null, prev = null) {
      this.url = url;
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
      this.activeNode = new DoublyLinkedNode(homepage);
   }

   visit(url) {
      const node = this.activeNode;
      node.next = new DoublyLinkedNode(url, null, node);
      this.activeNode = node.next;
   }

   _cycle(steps, direction) {
      let node = this.activeNode;

      while (steps && node[direction]) {
         node = node[direction];
         steps--;
      }

      this.activeNode = node;
      return node.url;
   }

   back(steps) {
      return this._cycle(steps, 'prev');
   }

   forward(steps) {
      return this._cycle(steps, 'next');
   }
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
