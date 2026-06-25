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
    *     A: dfs, recursion, pre-order traversal
    * @param {TreeNode} root
    * @return {boolean}
    */
   evaluateTree = (root) => {
      const dfs = (node) => {
         if (node.val === 2) {
            return dfs(node.left) || dfs(node.right)
         } else if (node.val === 3) {
            return dfs(node.left) && dfs(node.right)
         } else {
            return Boolean(node.val);
         }
      }

      return dfs(root);
   }
}


const evaluateTree = new Solution().evaluateTree;
console.log(new Solution().evaluateTree(buildTree([0])) === false)
console.log(new Solution().evaluateTree(buildTree([1])) === true)
console.log(new Solution().evaluateTree(buildTree([2, 1, 3, null, null, 0, 1])) === true)
