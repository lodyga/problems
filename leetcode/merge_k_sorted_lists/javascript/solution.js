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
    * Time complexity: O(nlogk)
    * Auxiliary space complexity: O(k)
    * Tags: linked list
    * merge sort
    * @param {ListNode[]} lists
    * @return {ListNode}
    */
   mergeKLists(lists) {
      if (lists.length === 0) {
         return null
      }

      const mergeTwoLists = (node1, node2) => {
         const anchor = new ListNode();
         let node = anchor;

         while (node1 && node2) {
            if (node1.val < node2.val) {
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

      while (lists.length > 1) {
         const mergedLists = [];

         for (let index = 0; index < lists.length; index += 2) {
            const head1 = lists[index];
            const head2 = index + 1 < lists.length ? lists[index + 1] : null;
            mergedLists.push(mergeTwoLists(head1, head2));
         }
         lists = mergedLists;
      }
      return lists[0]
   };
}
const mergeKLists = new Solution().mergeKLists;


console.log(getLinkedListValues(new Solution().mergeKLists([buildLinkedList([1, 4, 5]), buildLinkedList([1, 3, 4]), buildLinkedList([2, 6])])), [1, 1, 2, 3, 4, 4, 5, 6])
console.log(getLinkedListValues(new Solution().mergeKLists([buildLinkedList([1, 4, 5])])), [1, 4, 5])
console.log(getLinkedListValues(new Solution().mergeKLists([])), [])
console.log(getLinkedListValues(new Solution().mergeKLists([buildLinkedList([])])), [])