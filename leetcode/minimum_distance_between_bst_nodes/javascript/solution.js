import { TreeNode, buildTree } from '../../../../JS/binary-tree.js';


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
    * Auxiliary space complexity: O(n)
    * Tags: binary tree
    * @param {TreeNode} root
    * @return {number}
    */
   minDiffInBST(root) {
      let minDiff = 10e5 + 1;
      let prevNode = null;

      const dfs = (node) => {
         if (!node)
            return

         dfs(node.left);
         if (prevNode)
            minDiff = Math.min(minDiff, node.val - prevNode.val);
         prevNode = node;
         dfs(node.right);
      };
      
      dfs(root);
      return minDiff
   };
}


const minDiffInBST = new Solution().minDiffInBST;
console.log(new Solution().minDiffInBST(buildTree([3, null, 6])) === 3)
console.log(new Solution().minDiffInBST(buildTree([4, 2, 6, 1, 3])) === 1)
console.log(new Solution().minDiffInBST(buildTree([1, 0, 48, null, null, 12, 49])) === 1)
console.log(new Solution().minDiffInBST(buildTree([90, 69, null, 49, 89, null, 52])) === 1)
console.log(new Solution().minDiffInBST(buildTree([41, 19, 62, 11, 31, null, 89, 8, 18, null, null, 74, null, null, null, 16])) === 1)