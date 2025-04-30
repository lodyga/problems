class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: linked list
    * @param {ListNode} node1
    * @param {ListNode} node2
    * @return {ListNode}
    */
   mergeTwoLists(node1, node2) {
      let node = new ListNode();
      let anchor = node;

      while (
         node1 && node2
      ) {
         if (node1.val <= node2.val) {
            node.next = node1;
            node1 = node1.next;
         } else {
            node.next = node2;
            node2 = node2.next;
         }
         node = node.next;
      }

      node.next = node1 || node2;
      return anchor.next
   }
}
const mergeTwoLists = new Solution().mergeTwoLists;


console.log(getLinkedListValues(new Solution().mergeTwoLists(buildLinkedList([]), buildLinkedList([]))), [])
console.log(getLinkedListValues(new Solution().mergeTwoLists(buildLinkedList([]), buildLinkedList([0]))), [0])
console.log(getLinkedListValues(new Solution().mergeTwoLists(buildLinkedList([1, 2, 4]), buildLinkedList([1, 3, 4]))), [1, 1, 2, 3, 4, 4])