class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: linked list
    * @param {ListNode} head
    * @return {ListNode}
    */
   removeNodes(head) {
      let slow = head;
      let fast = head;
      while (fast) {
         slow = slow.next;
         fast = fast.next.next;
      }

      let node = slow;
      let prev = null;
      while (node) {
         const nodeNext = node.next;
         node.next = prev;
         prev = node;
         node = nodeNext;
      }
      
      let twinSum = 0;
      let left = head;
      let right = prev;
      while (right) {
         twinSum = Math.max(twinSum, left.val + right.val);
         left = left.next;
         right = right.next;
      }
      return twinSum
   };
}
const removeNodes = new Solution().removeNodes;


console.log(new Solution().removeNodes(buildLinkedList([5, 4, 2, 1])) === 6)
console.log(new Solution().removeNodes(buildLinkedList([4, 2, 2, 3])) === 7)
console.log(new Solution().removeNodes(buildLinkedList([1, 100000])) === 100001)