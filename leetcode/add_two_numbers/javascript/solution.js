class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: linked list, iteration
    * @param {ListNode} head1
    * @param {ListNode} head2
    * @return {ListNode}
    */
   addTwoNumbers = function (head1, head2) {
      function add(node1, node2, carry) {
         if (!node1 && !node2 && carry === 0) {
            return null
         }
         let val = (
            (node1 ? node1.val : 0 )+ 
            (node2 ? node2.val : 0) + 
            carry
         );
         carry = val > 9 ? 1 : 0;
         val = val % 10;
         const node = new ListNode(val);
         node.next = add(
            node1 ? node1.next : null,
            node2 ? node2.next : null,
            carry
         );
         return node
      }
      return add(head1, head2, 0)
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: linked list, recursion
    * @param {ListNode} head1
    * @param {ListNode} head2
    * @return {ListNode}
    */
   addTwoNumbers = function (head1, head2) {
      const anchor = new ListNode();
      let node = anchor;
      let carry = 0;
      while (head1 || head2) {
         let val = (
            (head1 ? head1.val : 0) +
            (head2 ? head2.val : 0) +
            carry
         )
         carry = val > 9 ? 1 : 0;
         val = val > 9 ? val - 10 : val;
         node.next = new ListNode(val);
         node = node.next;
         head1 = head1 ? head1.next : null;
         head2 = head2 ? head2.next : null;
      }
      if (carry) {
         node.next = new ListNode(1);
      }
      return anchor.next
   };
}
const addTwoNumbers = new Solution().addTwoNumbers;


console.log(getLinkedListValues(new Solution().addTwoNumbers(buildLinkedList([2, 4, 3]), buildLinkedList([5, 6, 4]))), [7, 0, 8])
console.log(getLinkedListValues(new Solution().addTwoNumbers(buildLinkedList([0]), buildLinkedList([0]))), [0])
console.log(getLinkedListValues(new Solution().addTwoNumbers(buildLinkedList([9, 9, 9, 9, 9, 9, 9]), buildLinkedList([9, 9, 9, 9]))),  [8, 9, 9, 9, 0, 0, 0, 1])