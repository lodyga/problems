class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: linked list
    * @param {ListNode} head
    * @return {ListNode}
    */
   deleteDuplicates(head) {
      let node = head;

      while (node && node.next) {
         while (
            node.next &&
            node.next.val === node.val
         ) {
            node.next = node.next.next;
         }
         if (node.next) {
            node = node.next;
         }
      }
      return head;
   };
}
const deleteDuplicates = new Solution().deleteDuplicates;


console.log(getLinkedListValues(new Solution().deleteDuplicates(buildLinkedList([]))), [])
console.log(getLinkedListValues(new Solution().deleteDuplicates(buildLinkedList([1, 1, 2]))), [1, 2])
console.log(getLinkedListValues(new Solution().deleteDuplicates(buildLinkedList([1, 1, 2, 3, 3]))), [1, 2, 3])