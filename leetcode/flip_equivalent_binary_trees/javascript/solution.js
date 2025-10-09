import { TreeNode, buildTree } from '../../../../JS/binary-tree.js';


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
    * Tags: binary tree
    * @param {TreeNode} root1
    * @param {TreeNode} root2
    * @return {boolean}
    */
   flipEquiv(root1, root2) {
      const dfs = (node1, node2) => {
         if (node1 === null || node2 === null)
            return (node1 === null && node2 === null)
         else if (node1.val !== node2.val)
            return false

         const noFlip = (
            dfs(node1.left, node2.left) &&
            dfs(node1.right, node2.right)
         );
         const flip = (
            dfs(node1.left, node2.right) &&
            dfs(node1.right, node2.left)
         );
         return noFlip || flip
      }
      return dfs(root1, root2)
   };
}


const flipEquiv = new Solution().flipEquiv;
console.log(new Solution().flipEquiv(buildTree([1]), buildTree([1])) === true)
console.log(new Solution().flipEquiv(buildTree([1, 2, 3, 4, 5, 6, null, null, null, 7, 8]), buildTree([1, 3, 2, null, 6, 4, 5, null, null, null, null, 8, 7])) === true)
console.log(new Solution().flipEquiv(buildTree([]), buildTree([])) === true)
console.log(new Solution().flipEquiv(buildTree([]), buildTree([1])) === false)