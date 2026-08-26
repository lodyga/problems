import { ListNode, LinkedList } from '../../../../JS/linked-list-utils.js'


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: linked list
    *     A: iteration
    * Reverse a singly-linked list.
    * @param {ListNode} head
    * @return {ListNode}
    */
   reverseList(head) {
      let node = head;
      let prev = null;

      while (node) {
         const nodeNext = node.next;
         node.next = prev;
         prev = node;
         node = nodeNext;
      }
      
      return prev
   }
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: linked list
    *     A: iteration
    * Reverse a singly-linked list.
    * One-liner
    * @param {ListNode} head
    * @return {ListNode}
    */
   reverseList(head) {
      let node = head;
      let prev = null;

      while (node) {
         [node.next, prev, node] = [prev, node, node.next]
      }
      return prev
   }
}

const linkedList = new LinkedList();
const buildLinkedList = linkedList.buildLinkedList;
const serializeLinkedList = linkedList.serializeLinkedList;
const areLinkedListsEqueal = linkedList.areLinkedListsEqueal;
const solution = new Solution();
const reverseList = new Solution().reverseList;

console.log(JSON.stringify(new LinkedList().serializeLinkedList(new Solution().reverseList(new LinkedList().buildLinkedList([])))) === JSON.stringify([]))
console.log(JSON.stringify(new LinkedList().serializeLinkedList(new Solution().reverseList(new LinkedList().buildLinkedList([1, 2, 3, 4, 5])))))

console.log(JSON.stringify(serializeLinkedList(solution.reverseList(buildLinkedList([1, 2])))) === JSON.stringify([2, 1]))
console.log(JSON.stringify(serializeLinkedList(solution.reverseList(buildLinkedList([1, 2, 3, 4, 5])))) === JSON.stringify([5, 4, 3, 2, 1]))
