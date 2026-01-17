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
    * Time complexity: O(n)e
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: binary tree
    *     A: dfs, recursion, pre-order traversal
    * @param {TreeNode} root
    * @return {string}
    */
   tree2str(root) {
      const parts = [];

      const dfs = (node) => {
         if (node === null) {
            return
         }
         parts.push(node.val);

         if (node.left || node.right) {
            parts.push('(');
            dfs(node.left);
            parts.push(')');
         }
         if (node.right) {
            parts.push('(');
            dfs(node.right);
            parts.push(')');
         }
      }
      dfs(root);
      return parts.join('')
   };

   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: binary tree
    *     A: dfs, recursion, pre-order traversal
    * @param {TreeNode} root
    * @return {string}
    */
   tree2str(root) {
      const dfs = (node) => {
         if (node === null) {
            return ''
         }
         let res = String(node.val);

         if (node.left || node.right)
            res += '(' + dfs(node.left) + ')'

         if (node.right)
            res += '(' + dfs(node.right) + ')'

         return res
      }
      return dfs(root)
   }
}


const tree2str = new Solution().tree2str;
console.log(new Solution().tree2str(buildTree([1])) === '1')
console.log(new Solution().tree2str(buildTree([1, 2])) === '1(2)')
console.log(new Solution().tree2str(buildTree([1, null, 3])) === '1()(3)')
console.log(new Solution().tree2str(buildTree([1, 2, 3])) === '1(2)(3)')
console.log(new Solution().tree2str(buildTree([1, 2, 3, 4])) === '1(2(4))(3)')
console.log(new Solution().tree2str(buildTree([1, 2, 3, null, 4])) === '1(2()(4))(3)')
