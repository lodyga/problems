class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: linked list
    * @param {ListNode} head
    * @param {number} val
    * @return {ListNode}
    */
   removeElements(head, val) {
      const anchor = new ListNode(null, head);
      let node = anchor;

      while (node.next) {
         while (
            node.next && 
            node.next.val === val
         ) {
            node.next = node.next.next;
         }
         if (node.next) {
            node = node.next;
         }
      }
      return anchor.next
   };
}
const removeElements = new Solution().removeElements;


console.log(getLinkedListValues(new Solution().removeElements(buildLinkedList([1, 2, 6, 3, 4, 5, 6]), 6)), [1, 2, 3, 4, 5])
console.log(getLinkedListValues(new Solution().removeElements(buildLinkedList([]), 1)), [])
console.log(getLinkedListValues(new Solution().removeElements(buildLinkedList([7, 7, 7, 7]), 7)), [])