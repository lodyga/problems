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
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, dfs, recursion
    * @param {TreeNode} root1
    * @param {TreeNode} root2
    * @return {boolean}
    */
   isSubtree(root1, root2) {
      if (!root2) {
         return true
      } else if (!root1) {
         return false
      } else if (this.isSameTree(root1, root2)) {
         return true
      }
      return (
         this.isSubtree(root1.left, root2) ||
         this.isSubtree(root1.right, root2)
      )
   };

   isSameTree(root1, root2) {
      if (!root1 && !root2) {
         return true
      } else if (
         root1 &&
         root2 &&
         root1.val === root2.val
      ) {
         return (
            this.isSameTree(root1.left, root2.left) &&
            this.isSameTree(root1.right, root2.right)
         )
      } else {
         return false
      }
   }
}


console.log(new Solution().isSubtree(buildTree([3, 4, 5, 1, 2]), buildTree([4, 1, 2])), true)
console.log(new Solution().isSubtree(buildTree([3, 4, 5, 1, 2, null, null, null, null, 0]), buildTree([4, 1, 2])), false)