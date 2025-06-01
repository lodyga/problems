class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: linked list
    * @param {ListNode} head1
    * @param {number} a
    * @param {number} b
    * @param {ListNode} head2
    * @return {ListNode}
    */
   mergeInBetween = function (head1, a, b, head2) {
      const anchor = new ListNode(null, head1);
      let node = anchor;

      while (a) {
         node = node.next;
         a--;
         b--;
      }
      const startNode = node;

      while (b + 2) {
         node = node.next
         b--;
      }
      const endNode = node;

      node = head2;
      while (node.next) {
         node = node.next;
      }
      node.next = endNode;

      startNode.next = head2

      return anchor.next
   };
}
const mergeInBetween = new Solution().mergeInBetween;


console.log(getLinkedListValues(new Solution().mergeInBetween(buildLinkedList([10, 1, 13, 6, 9, 5]), 3, 4, buildLinkedList([1000000, 1000001, 1000002]))), [10, 1, 13, 1000000, 1000001, 1000002, 5])
console.log(getLinkedListValues(new Solution().mergeInBetween(buildLinkedList([0, 1, 2, 3, 4, 5, 6]), 2, 5, buildLinkedList([1000000, 1000001, 1000002, 1000003, 1000004]))), [0, 1, 1000000, 1000001, 1000002, 1000003, 1000004, 6])