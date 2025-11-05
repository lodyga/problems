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
   static isSubtree(root1, root2) {
      const isSameTree = (root1, root2) => {
         if (root1 === null && root2 === null) {
            return true
         } else if (root1 === null || root2 === null) {
            return false
         } else if (root1.val !== root2.val) {
            return false
         }
         return (
            isSameTree(root1.left, root2.left) &&
            isSameTree(root1.right, root2.right)
         )
      }

      if (root2 === null) {
         return true
      } else if (root1 === null) {
         return false
      } else if (isSameTree(root1, root2)) {
         return true
      }
      return (
         isSubtree(root1.left, root2) ||
         isSubtree(root1.right, root2)
      )
   };

}


const isSubtree = Solution.isSubtree;
console.log(Solution.isSubtree(buildTree([3, 4, 5, 1, 2]), buildTree([4, 1, 2])) === true)
console.log(Solution.isSubtree(buildTree([3, 4, 5, 1, 2, null, null, null, null, 0]), buildTree([4, 1, 2])) === false)