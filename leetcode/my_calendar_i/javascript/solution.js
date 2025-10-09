class ListNode {
   constructor(start = null, end = null, next = null) {
      this.start = start;
      this.end = end;
      this.next = next;
   }
}


/**
 * Time complexity: O(n)
 * Auxiliary space complexity: O(n)
 * Tags: linked list
 */
class MyCalendar {
   constructor() {
      this.anchor = new ListNode();
   };

   /** 
   * @param {number} start 
   * @param {number} end
   * @return {boolean}
   */
   book(start, end) {
      let node = this.anchor;

      while (node.next) {
         if (
            start < node.next.end &&
            end > node.next.start
         ) return false
         else if (end <= node.next.start)
            break
         else if (start >= node.next.end)
            node = node.next;
      }
      const newNode = new ListNode(start, end, node.next);
      node.next = newNode;
      return true
   }
}


class TreeNode {
   constructor(start = null, end = null, left = null, right = null) {
      this.start = start
      this.end = end
      this.left = left
      this.right = right

   }
}


/**
 * Time complexity: O(n)
 * Auxiliary space complexity: O(n)
 * Tags: binary tree, recursion
 */
class MyCalendar {
   constructor() {
      this.root = null;
   };

   /** 
   * @param {number} start 
   * @param {number} end
   * @return {boolean}
   */
   book(start, end) {
      if (!this.root) {
         this.root = new TreeNode(start, end);
         return true
      }
      return this._insert(this.root, start, end)
   };

   _insert(node, start, end) {
      if (start >= node.end) {
         if (node.right)
            return this._insert(node.right, start, end)
         else {
            node.right = new TreeNode(start, end);
            return true
         }
      } else if (end <= node.start) {
         if (node.left)
            return this._insert(node.left, start, end)
         else {
            node.left = new TreeNode(start, end);
            return true
         }
      } else 
         return false
   }
}


const myCalendar = new MyCalendar();
console.log(myCalendar.book(10, 20));  // return True
console.log(myCalendar.book(15, 25));  // return False, It can not be booked because time 15 is already booked by another event.
console.log(myCalendar.book(20, 30));  // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.