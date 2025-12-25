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
    * Tags: 
    *     DS: linked list, hash map
    *     A: iteration
    * @param {_Node} head
    * @return {_Node}
    */
   copyRandomList(head) {
      const nodeMap = new Map([[null, null]]);
      
      let node = head;
      while (node) {
         const nodeCopy = new _Node(node.val);
         nodeMap.set(node, nodeCopy);
         node = node.next;
      }

      node = head;
      while (node) {
         const nodeCopy = nodeMap.get(node);
         nodeCopy.next = nodeMap.get(node.next);
         nodeCopy.random = nodeMap.get(node.random);
         node = node.next;
      }
      return nodeMap.get(head);
   };
}


const copyRandomList = new Solution().copyRandomList;