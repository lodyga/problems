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
    * @return {number}
    */
   diameterOfBinaryTree(root) {
      let diameter = 0;

      const dfs = (node) => {
         if (node === null) {
            return 0
         }
         const left = dfs(node.left);
         const right = dfs(node.right);
         diameter = Math.max(diameter, left + right);

         return 1 + Math.max(left, right)
      }

      dfs(root);
      return diameter
   };
}


const diameterOfBinaryTree = new Solution().diameterOfBinaryTree;
console.log(new Solution().diameterOfBinaryTree(buildTree([5])) === 0)
console.log(new Solution().diameterOfBinaryTree(buildTree([1, 2])) === 1)
console.log(new Solution().diameterOfBinaryTree(buildTree([1, 2, 3])) === 2)
console.log(new Solution().diameterOfBinaryTree(buildTree([1, 2, 3, 4, 5])) === 3)
