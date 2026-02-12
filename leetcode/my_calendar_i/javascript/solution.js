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
 * Tags:
 *     DS: linked list
 *     A: interval, iteration
 */
class MyCalendar1 {
   constructor() {
      this.calendar = new ListNode();
   };

   /** 
   * @param {number} start 
   * @param {number} end
   * @return {boolean}
   */
   book(start, end) {
      let node = this.calendar;

      while (node.next) {
         // New booking starts before current node.
         if (end <= node.next.start) {
            break
            // New booking starts after current node.
         } else if (start >= node.next.end) {
            node = node.next;
            // New booking overlaps current node.
         } else if (
            start < node.next.end &&
            end > node.next.start
         ) {
            return false
         }
      }

      node.next = new ListNode(start, end, node.next);
      return true
   }
}


class TreeNode {
   constructor(start = null, end = null, left = null, right = null) {
      this.start = start;
      this.end = end;
      this.left = left;
      this.right = right;

   }
}


/**
 * Time complexity: O(n)
 * Auxiliary space complexity: O(n)
 * Tags:
 *     DS: binary tree, BST
 *     A: interval, iteration
 */
class MyCalendar {
   constructor() {
      this.calendar = null;
   };

   /** 
   * @param {number} start 
   * @param {number} end
   * @return {boolean}
   */
   book(start, end) {
      if (this.calendar === null) {
         this.calendar = new TreeNode(start, end)
         return true
      }

      let node = this.calendar;

      while (true) {
         // New booking starts after current node.
         if (start >= node.end) {
            if (node.right) {
               node = node.right;
            } else {
               node.right = new TreeNode(start, end);
               return true
            }
            // New booking starts before current node.
         } else if (end <= node.start) {
            if (node.left) {
               node = node.left
            } else {
               node.left = new TreeNode(start, end)
               return true
            }
            // New booking overlaps current node.
         } else {
            return false
         }
      }
   }
}


/**
 * Time complexity: O(n)
 * Auxiliary space complexity: O(n)
 * Tags:
 *     DS: binary tree, BST
 *     A: interval, recursion
 */
class MyCalendar {
   constructor() {
      this.calendar = null;
   };

   /** 
   * @param {number} start 
   * @param {number} end
   * @return {boolean}
   */
   book(start, end) {
      if (this.calendar === null) {
         this.calendar = new TreeNode(start, end);
         return true
      } else {
         return this._insert(this.calendar, start, end);
      }
   };

   _insert(node, start, end) {
      // New booking starts after current node.
      if (start >= node.end) {
         if (node.right) {
            return this._insert(node.right, start, end)
         } else {
            node.right = new TreeNode(start, end);
            return true
         }
         // New booking starts before current node.
      } else if (end <= node.start) {
         if (node.left) {
            return this._insert(node.left, start, end)
         } else {
            node.left = new TreeNode(start, end)
            return true
         }
         // New booking overlaps current node.
      } else {
         return false
      }
   };
}


// Example 1
let myCalendar = new MyCalendar();
console.log(myCalendar.book(10, 20) === true);
console.log(myCalendar.book(15, 25) === false);
console.log(myCalendar.book(20, 30) === true);

// Example 2
myCalendar = new MyCalendar();
console.log(myCalendar.book(47, 50) === true);
console.log(myCalendar.book(33, 41) === true);
console.log(myCalendar.book(39, 45) === false);
console.log(myCalendar.book(33, 42) === false);
console.log(myCalendar.book(25, 32) === true);
console.log(myCalendar.book(26, 35) === false);
console.log(myCalendar.book(19, 25) === true);
console.log(myCalendar.book(3, 8) === true);
console.log(myCalendar.book(8, 13) === true);
console.log(myCalendar.book(18, 27) === false);
