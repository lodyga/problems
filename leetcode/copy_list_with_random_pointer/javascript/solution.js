class _Node {
   constructor(val, next, random) {
      this.val = val;
      this.next = next;
      this.random = random;
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: linked list, hash map
    * @param {_Node} head
    * @return {_Node}
    */
   copyRandomList(head) {
      const originalToCopy = new Map([[null, null]]);
      let node = head;
      while (node) {
         originalToCopy.set(node, new _Node(node.val));
         node = node.next;
      }

      node = head;
      while (node) {
         originalToCopy.get(node).next = originalToCopy.get(node.next);
         originalToCopy.get(node).random = originalToCopy.get(node.random);
         node = node.next;
      }

      return originalToCopy.get(head);
   };
}