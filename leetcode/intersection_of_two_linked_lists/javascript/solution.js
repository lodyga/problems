class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: linked list
    * @param {TreeNode} headA
    * @param {TreeNode} headB
    * @return {boolean}
    */
   getIntersectionNode(headA, headB) {
      function getLenght(node) {
         let listLength = 0;
         while (node) {
            listLength++;
            node = node.next;
         }
         return listLength
      };

      const listALength = getLenght(headA);
      const listBLength = getLenght(headB);
      const lengthDiff = Math.abs(listALength - listBLength);
      let nodeA = headA;
      let nodeB = headB;

      if (listALength > listBLength) {
         for (let index = 0; index < lengthDiff; index++) {
            nodeA = nodeA.next;
         }
      } else if (listBLength > listALength) {
         for (let index = 0; index < lengthDiff; index++) {
            nodeB = nodeB.next;
         }
      }
      while (nodeA && nodeB) {
         if (nodeA === nodeB) {
            return nodeA
         }
         nodeA = nodeA.next;
         nodeB = nodeB.next;
      }
      return null
   };
}
const getIntersectionNode = new Solution().getIntersectionNode;


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: linked list
    * @param {TreeNode} headA
    * @param {TreeNode} headB
    * @return {boolean}
    */
   getIntersectionNode = function (headA, headB) {
      let nodeA = headA;
      let nodeB = headB;

      while (nodeA != nodeB) {
         nodeA = nodeA ? nodeA.next : headB;
         nodeB = nodeB ? nodeB.next : headA;
      }

      return nodeA
   };
}
const getIntersectionNode = new Solution().getIntersectionNode;