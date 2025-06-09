class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: linked list, two pointers
    * three pass
    * @param {ListNode} head
    * @param {number} k
    * @return {ListNode}
    */
   swapNodes(head, k) {
      let node = head;
      let prev = null;
      let index = 1;
      let val;
      while (node) {
         if (index === k) {
            val = node.val;
         }
         index++;
         const nodeNext = node.next;
         node.next = prev;
         prev = node;
         node = nodeNext;
      }
      
      node = prev;
      prev = null;
      index = 1;
      while (node) {
         if (index === k) {
            [val, node.val] = [node.val, val];
         }
         index++;
         const nodeNext = node.next;
         node.next = prev;
         prev = node;
         node = nodeNext;
      }
      
      node = head;
      prev = null;
      index = 1;
      while (node) {
         if (index === k) {
            node.val = val;
            break
         }
         index++;
         node = node.next;
      }

      return head
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: linked list, two pointers
    * two pass
    * @param {ListNode} head
    * @param {number} k
    * @return {ListNode}
    */
   swapNodes(head, k) {
      let node = head;
      let left;
      let right;
      
      let listLength = 0
      while (node) {
         listLength++;
         node = node.next;
      }

      let index = 1;
      node = head;
      while (node) {
         if (index === k) {
            left = node;
         }
         if (index === listLength - k + 1) {
            right = node;
            break
         }
         node = node.next;
         index++;
      }

      [left.val, right.val] = [right.val, left.val];
      return head
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: linked list, two pointers
    * one pass
    * @param {ListNode} head
    * @param {number} k
    * @return {ListNode}
    */
   swapNodes(head, k) {
      let node = head;
      let left = head;
      let right = head;

      for (let index = 1; index < k; index++) {
         node = node.next;
         left = left.next;
      }

      while (node.next) {
         node = node.next;
         right = right.next;
      }

      [left.val, right.val] = [right.val, left.val];
      return head
   };
}
const swapNodes = new Solution().swapNodes;


console.log(getLinkedListValues(new Solution().swapNodes(buildLinkedList([1, 2, 3, 4]), 2)), [1, 3, 2, 4])
console.log(getLinkedListValues(new Solution().swapNodes(buildLinkedList([1, 2, 3, 4, 5]), 2)), [1, 4, 3, 2, 5])
console.log(getLinkedListValues(new Solution().swapNodes(buildLinkedList([7, 9, 6, 6, 7, 8, 3, 0, 9, 5]), 5)), [7, 9, 6, 6, 8, 7, 3, 0, 9, 5])