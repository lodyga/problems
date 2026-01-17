import { ListNode, areLinkedListsEqueal, buildLinkedList, getLinkedListValues } from '../../../../JS/linked-list-utils.js'


/**
 * Represents a node in a singly-linked list.
 * class ListNode {
 *    constructor(val = null, next = null) {
 *       this.val = val;
 *       this.next = next;
 *    }
 * }
 */


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: linked list
    *     A: iteration
    * @param {ListNode} head1
    * @param {ListNode} head2
    * @return {ListNode}
    */
   addTwoNumbers(head1, head2) {
      const anchor = new ListNode();
      let node = anchor;
      let carry = 0;
      let node1 = head1;
      let node2 = head2;

      while (node1 || node2 || carry) {
         const val1 = node1 ? node1.val : 0;
         const val2 = node2 ? node2.val : 0;
         let val = val1 + val2 + carry;
         carry = val > 9 ? 1 : 0;
         val = val > 9 ? val - 10 : val;
         node.next = new ListNode(val);
         node1 = node1 ? node1.next : null;
         node2 = node2 ? node2.next : null;
         node = node.next;
      }
      return anchor.next
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: linked list
    *     A: retursion
    * @param {ListNode} head1
    * @param {ListNode} head2
    * @return {ListNode}
    */
   addTwoNumbers(head1, head2) {
      const add = (node1, node2, carry) => {
         if (
            node1 === null &&
            node2 === null &&
            carry === 0
         ) {
            return null
         }
         const val1 = node1 ? node1.val : 0;
         const val2 = node2 ? node2.val : 0;
         let val = val1 + val2 + carry;
         carry = val > 9 ? 1 : 0;
         val = val > 9 ? val - 10 : val;
         let node = new ListNode(val);
         node1 = node1 ? node1.next : null;
         node2 = node2 ? node2.next : null;
         node.next = add(node1, node2, carry);
         return node
      }
      return add(head1, head2, 0)
   };
}


const addTwoNumbers = new Solution().addTwoNumbers;
console.log(areLinkedListsEqueal(new Solution().addTwoNumbers(buildLinkedList([2, 4, 3]), buildLinkedList([5, 6, 4])), buildLinkedList([7, 0, 8])))
console.log(areLinkedListsEqueal(new Solution().addTwoNumbers(buildLinkedList([0]), buildLinkedList([0])), buildLinkedList([0])))
console.log(areLinkedListsEqueal(new Solution().addTwoNumbers(buildLinkedList([9, 9, 9, 9, 9, 9, 9]), buildLinkedList([9, 9, 9, 9])), buildLinkedList([8, 9, 9, 9, 0, 0, 0, 1])))
