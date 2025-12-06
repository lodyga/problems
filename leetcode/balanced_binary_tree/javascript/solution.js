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
    *     A: dfs, recursion
    * @param {TreeNode} root
    * @return {boolean}
    */
   isBalanced(root) {
      let isTreeBalanced = true;

      const dfs = (node) => {
         if (node === null) {
            return 0
         }
         const left = dfs(node.left);
         const right = dfs(node.right);

         if (Math.abs(left - right) > 1) {
            isTreeBalanced = false;
         }
         return 1 + Math.max(left, right)
      }
      dfs(root);
      return isTreeBalanced
   };
}


const isBalanced = new Solution().isBalanced;
console.log(new Solution().isBalanced(buildTree([3])) === true)
console.log(new Solution().isBalanced(buildTree([1, 2, 3])) === true)
console.log(new Solution().isBalanced(buildTree([3, 9, 20, null, null, 15, 7])) === true)
console.log(new Solution().isBalanced(buildTree([1, 2, 2, 3, 3, null, null, 4, 4])) === false)
console.log(new Solution().isBalanced(buildTree([1, 2, 2, 3, null, null, 3, 4, null, null, 4])) === false)
console.log(new Solution().isBalanced(buildTree([])) === true)
