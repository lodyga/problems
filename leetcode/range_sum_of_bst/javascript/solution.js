import { TreeNode, buildTree, getTreeValues } from '../../../../JS/binary-tree.js';


/**
 * class TreeNode {
 *    constructor(val = null, left = null, right = null) {
 *       this.val = val
 *       this.left = left
 *       this.right = right
 *    };
 * }
 */


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, dfs, recursion
    * @param {TreeNode} root
    * @param {number} low
    * @param {number} high
    * @return {number}
    */
   rangeSumBST(root, low, high) {
      let rangeSum = 0;

      function dfs(node) {
         if (!node) return 0
         if (
            node.val >= low &&
            node.val <= high
         ) rangeSum += node.val;
         if (node.val > low) dfs(node.left);
         if (node.val < high) dfs(node.right);
      }
      dfs(root);
      return rangeSum
   };
}
const rangeSumBST = new Solution().rangeSum;


console.log(new Solution().rangeSumBST(buildTree([10, 5, 15, 3, 7, null, 18]), 7, 15), 32)
console.log(new Solution().rangeSumBST(buildTree([10, 5, 15, 3, 7, 13, 18, 1, null, 6]), 6, 10), 23)