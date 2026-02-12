import { ListNode, buildLinkedList, getLinkedListValues } from '../../../../JS/linked-list-utils.js'


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
    *     DS: linked list, list
    *     A: iteration
    * @param {ListNode} head
    * @param {number} k
    * @return {ListNode[]}
    */
   splitListToParts(head, k) {
      let node = head
      let len = 0;

      while (node) {
         len++;
         node = node.next;
      }

      const partLen = Math.floor(len / k);
      let rest = len % k;

      node = head;
      const res = [];

      for (let i = 0; i < k; i++) {
         res.push(node);

         if (node === null)
            continue

         for (let i = 0; i < partLen - 1 + (rest ? 1 : 0); i++)
            node = node.next;

         rest -= rest ? 1 : 0;
         const nodeNext = node.next;
         node.next = null;
         node = nodeNext;
      }

      return res
   };
}


const splitListToParts = new Solution().splitListToParts;
console.log(new Solution().splitListToParts(buildLinkedList([1, 2, 3]), 5), )
console.log(new Solution().splitListToParts(buildLinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3), )
