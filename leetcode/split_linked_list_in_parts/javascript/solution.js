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
    * Tags: linked list
    * @param {ListNode} head
    * @param {number} k
    * @return {ListNode[]}
    */
   splitListToParts(head, k) {
      let node = head;
      let len = 0;
      while (node) {
         len++;
         node = node.next
      }
      const div = Math.floor(len / k);
      let mod = len % k;

      node = head;
      const heads = [];
      for (let index = 0; index < k; index++) {
         heads.push(node);
         let rng = 0;
         if (mod) {
            rng = div + 1;
            mod -= 1;
         }
         else
            rng = div;

         while (rng) {
            if (rng === 1) {
               [node.next, node] = [null, node.next]  // right order
               // [node, node.next] = [node.next, null]  // wrong order
               // const nodeNext = node.next;
               // node.next = null;
               // node = nodeNext;

            } else
               node = node.next;
            rng--;
         }
      }

      return heads;
   };
}


const splitListToParts = new Solution().splitListToParts;
console.log(new Solution().splitListToParts(buildLinkedList([1, 2, 3]), 5),)
console.log(new Solution().splitListToParts(buildLinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3),)