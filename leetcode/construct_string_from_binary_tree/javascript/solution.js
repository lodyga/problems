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
    * @return {string}
    */
   tree2str(root) {
      const values = [];
      dfs(root);
      return values.join('')

      function dfs(node) {
         if (!node) {
            return
         }
         
         values.push(node.val);

         if (node.left || node.right) {
            values.push('(');
            dfs(node.left);
            values.push(')');
         }
         if (node.right) {
            values.push('(');
            dfs(node.right);
            values.push(')');
         }
      }
   };
}
const tree2str = new Solution().tree2str;


console.log(new Solution().tree2str(buildTree([1])) === '1')
console.log(new Solution().tree2str(buildTree([1, 2, 3, 4])) === '1(2(4))(3)')
console.log(new Solution().tree2str(buildTree([1, 2, 3, null, 4])) === '1(2()(4))(3)')