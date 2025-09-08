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
    * @param {TreeNode} root1
    * @param {TreeNode} root2
    * @return {TreeNode}
    */
   mergeTrees(root1, root2) {
      if (!root1) {
         return root2
      } else if (!root2) {
         return root1
      }
      const node = new TreeNode(root1.val + root2.val);
      node.left = this.mergeTrees(root1.left, root2.left)
      node.right = this.mergeTrees(root1.right, root2.right)
      return node
   };
}


console.log(geTreeValues(Solution().mergeTrees(buildTree([1]), buildTree([1, 2]))) == [2, 2])
console.log(geTreeValues(Solution().mergeTrees(buildTree([1, 2]), buildTree([1]))) == [2, 2])
console.log(geTreeValues(Solution().mergeTrees(buildTree([1, 3, 2, 5]), buildTree([2, 1, 3, None, 4, None, 7]))) == [3, 4, 5, 5, 4, None, 7])