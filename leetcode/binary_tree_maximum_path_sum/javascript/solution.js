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
    * Tags:
    *     DS: binary tree
    *     A: dfs, recursion, post-order traversal
    * @param {TreeNode} root
    * @return {int}
    */
   maxPathSum(root) {
      let maxPathSumValue = root.val;

      const dfs = (node) => {
         if (node === null)
            return 0

         const left = dfs(node.left);
         const right = dfs(node.right);
         const pathSum = node.val + left + right;
         maxPathSumValue = Math.max(maxPathSumValue, pathSum);
         return Math.max(0, node.val + Math.max(left, right))
      }
      dfs(root);
      return maxPathSumValue
   };
}


const maxPathSum = new Solution().maxPathSum;
console.log(new Solution().maxPathSum(buildTree([3])) === 3)
console.log(new Solution().maxPathSum(buildTree([-3])) === -3)
console.log(new Solution().maxPathSum(buildTree([4, 5, 6])) === 15)
console.log(new Solution().maxPathSum(buildTree([1, 2, 3])) === 6)
console.log(new Solution().maxPathSum(buildTree([4, -5, 6])) === 10)
console.log(new Solution().maxPathSum(buildTree([4, 5, -6])) === 9)
console.log(new Solution().maxPathSum(buildTree([-4, 5, 6])) === 7)
console.log(new Solution().maxPathSum(buildTree([-10, 9, 20, null, null, 15, 7])) === 42)
console.log(new Solution().maxPathSum(buildTree([1, -2, -3, 1, 3, -2, null, -1])) === 3)
console.log(new Solution().maxPathSum(buildTree([-15, 10, 20, null, null, 15, 5, -5])) === 40)
