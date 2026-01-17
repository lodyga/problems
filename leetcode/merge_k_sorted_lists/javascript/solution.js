import { ListNode, areLinkedListsEqueal, buildLinkedList, getLinkedListValues } from '../../../../JS/linked-list-utils.js'
import { PriorityQueue, MinPriorityQueue } from '@datastructures-js/priority-queue';

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

   /**
    * Time complexity: O(nlogk)
    *     n: total list nodes count
    * Auxiliary space complexity: O(k)
    * Tags:
    *     DS: linked list, heap
    *     A: iteration
    * @param {ListNode[]} lists
    * @return {ListNode}
    */
   mergeKLists(lists) {
      // const nodeHeap = new PriorityQueue((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]);
      const nodeHeap = new MinPriorityQueue(x => x[0]);
      for (const node of lists)
         if (node)
            nodeHeap.enqueue([node.val, node]);

      const anchor = new ListNode();
      let node = anchor;

      while (nodeHeap.size()) {
         const [, nextNode] = nodeHeap.dequeue();
         node.next = nextNode;
         node = node.next;

         if (nextNode.next)
            nodeHeap.enqueue([nextNode.next.val, nextNode.next]);
      }

      node.next = null;
      return anchor.next
   };

   /**
    * Time complexity: O(nlogk)
    *     n: total list nodes conunt
    *     k: list length
    * Auxiliary space complexity: O(logk)
    * Tags:
    *     DS: linked list, merge sort, divide and conquer
    *     A: recursion
    * @param {ListNode[]} lists
    * @return {ListNode}
    */
   static mergeKLists(lists) {
      const mergeTwoLists = (node1, node2) => {
         const anchor = new ListNode();
         let node = anchor;

         while (node1 && node2) {
            if (node1.val < node2.val) {
               node.next = node1;
               node = node.next;
               node1 = node1.next;
            } else {
               node.next = node2;
               node = node.next;
               node2 = node2.next;
            }
         }
         node.next = node1 || node2;
         return anchor.next
      };

      if (lists.length === 0) {
         return null
      } else if (lists.length === 1) {
         return lists[0]
      }

      // merge
      return mergeTwoLists(
         // divide
         mergeKLists(lists.slice(0, lists.length >> 1)),
         mergeKLists(lists.slice(lists.length >> 1,))
      )
   };
}


const mergeKLists = Solution.mergeKLists;
console.log(areLinkedListsEqueal(new Solution().mergeKLists([buildLinkedList([4, 5]), buildLinkedList([3, 4])]), buildLinkedList([3, 4, 4, 5])))
console.log(areLinkedListsEqueal(new Solution().mergeKLists([buildLinkedList([1, 4, 5]), buildLinkedList([1, 3, 4]), buildLinkedList([2, 6])]), buildLinkedList([1, 1, 2, 3, 4, 4, 5, 6])))
console.log(areLinkedListsEqueal(new Solution().mergeKLists([buildLinkedList([1, 4, 5])]), buildLinkedList([1, 4, 5])))
console.log(areLinkedListsEqueal(new Solution().mergeKLists([buildLinkedList([])]), buildLinkedList([])))
console.log(areLinkedListsEqueal(new Solution().mergeKLists([buildLinkedList([]), buildLinkedList([-1, 5, 11]), buildLinkedList([]), buildLinkedList([6, 10])]), buildLinkedList([-1, 5, 6, 10, 11])))
