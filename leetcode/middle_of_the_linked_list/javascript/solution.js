class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: linked list, two pointers
    * @param {ListNode} head
    * @return {ListNode}
    */
   middleNode(head) {
      let slow = head;
      let fast = head;

      while (fast && fast.next) {
         slow = slow.next;
         fast = fast.next.next;
      }
      return slow
   };
}
const middleNode = new Solution().middleNode;


console.log(getLinkedListValues(new Solution().middleNode(buildLinkedList([1, 2, 3, 4, 5]))), [3, 4, 5])
console.log(getLinkedListValues(new Solution().middleNode(buildLinkedList([1, 2, 3, 4, 5, 6]))), [4, 5, 6])