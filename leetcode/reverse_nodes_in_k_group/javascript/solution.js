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
    * @param {ListNode} head
    * @param {number} k
    * @return {ListNode}
    */
   reverseKGroup(head, k) {
      if (k === 1) return head

      const getKthOrNoneFromCurrentNode = (node, k) => {
         while (node && k) {
            node = node.next;
            k--;
         }
         return node
      };

      const reverseKNodesFromCurrenNode = (node, k) => {
         let prev = null;
         while (k) {
            const nodeNext = node.next;
            node.next = prev;
            prev = node;
            node = nodeNext;
            k -= 1;
         }
         return node
      };

      const anchor = new ListNode(null, head);
      let prev = anchor;
      let node = head;

      while (true) {
         const kthNode = getKthOrNoneFromCurrentNode(node, k - 1);
         prev.next = kthNode || node;
         if (kthNode === null)
            break

         const nextStartNode = reverseKNodesFromCurrenNode(node, k);
         prev = node;
         node = nextStartNode;
      }

      return anchor.next;
   };
}


const reverseKGroup = new Solution().reverseKGroup;
console.log(areLinkedListsEqueal(new Solution().reverseKGroup(buildLinkedList([1, 2, 3, 4, 5]), 2), buildLinkedList([2, 1, 4, 3, 5])))
console.log(areLinkedListsEqueal(new Solution().reverseKGroup(buildLinkedList([1, 2, 3, 4, 5]), 3), buildLinkedList([3, 2, 1, 4, 5])))
console.log(areLinkedListsEqueal(new Solution().reverseKGroup(buildLinkedList([1, 2, 3, 4, 5]), 1), buildLinkedList([1, 2, 3, 4, 5])))
console.log(areLinkedListsEqueal(new Solution().reverseKGroup(buildLinkedList([1, 2, 3, 4, 5]), 5), buildLinkedList([5, 4, 3, 2, 1])))
console.log(areLinkedListsEqueal(new Solution().reverseKGroup(buildLinkedList([1, 2, 3, 4, 5]), 4), buildLinkedList([4, 3, 2, 1, 5])))
console.log(areLinkedListsEqueal(new Solution().reverseKGroup(buildLinkedList([1, 2, 3, 4]), 2), buildLinkedList([2, 1, 4, 3])))
