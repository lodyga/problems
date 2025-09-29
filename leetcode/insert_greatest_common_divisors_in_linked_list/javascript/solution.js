import {ListNode, buildLinkedList, getLinkedListValues} from '../../../../JS/linked-list-utils.js'


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
    * Time complexity: O(nlog min(a, b))
    *     n: linked list length
    *     a, b: numbers for gcd
    * Auxiliary space complexity: O(1)
    * Tags: linked list, gcd
    * @param {ListNode} head
    * @return {number}
    */
   insertGreatestCommonDivisors(head) {
      // const gcd = (a, b) => b ? gcd(b, a % b) : a;
      const getGCD = (a, b) => {
         while (b !== 0) {
            [a, b] = [b, a % b]
         }
         return a
      };

      let node = head;
      while (node.next) {
         const gcd = getGCD(node.val, node.next.val)
         node.next = new ListNode(gcd, node.next);
         node = node.next.next;
      }
      return head
   };
}


const insertGreatestCommonDivisors = new Solution().insertGreatestCommonDivisors;
console.log(getLinkedListValues(new Solution().insertGreatestCommonDivisors(buildLinkedList([7]))), [7])
console.log(getLinkedListValues(new Solution().insertGreatestCommonDivisors(buildLinkedList([5, 10]))), [5, 5, 10])
console.log(getLinkedListValues(new Solution().insertGreatestCommonDivisors(buildLinkedList([18, 6, 10, 3]))), [18, 6, 6, 2, 10, 1, 3])