import { ListNode, buildLinkedList, areLinkedListsEqueal } from '../../../../JS/linked-list-utils.js'


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
    *     A: two pointers
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
console.log(areLinkedListsEqueal(new Solution().middleNode(buildLinkedList([1, 2, 3, 4, 5])), buildLinkedList([3, 4, 5])))
console.log(areLinkedListsEqueal(new Solution().middleNode(buildLinkedList([1, 2, 3, 4, 5, 6])), buildLinkedList([4, 5, 6])))
