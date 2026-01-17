import { TreeNode, buildTree, getTreeValues, isSameTree } from '../../../../JS/binary-tree.js';


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
    * @param {number} target
    * @returns {TreeNode}
    */
   removeLeafNodes(root, target) {
      if (root === null) {
         return null
      }

      root.left = removeLeafNodes(root.left, target);
      root.right = removeLeafNodes(root.right, target);

      if (
         root.val === target &&
         root.left === null &&
         root.right === null
      ) {
         return null
      }

      return root
   };
}


const removeLeafNodes = new Solution().removeLeafNodes;
console.log(isSameTree(new Solution().removeLeafNodes(buildTree([2]), 2), buildTree([])))
console.log(isSameTree(new Solution().removeLeafNodes(buildTree([3]), 2), buildTree([3])))
console.log(isSameTree(new Solution().removeLeafNodes(buildTree([3, 1, 2]), 2), buildTree([3, 1])))
console.log(isSameTree(new Solution().removeLeafNodes(buildTree([3, 2, 1]), 2), buildTree([3, null, 1])))
console.log(isSameTree(new Solution().removeLeafNodes(buildTree([2, 2, 2]), 2), buildTree([])))
console.log(isSameTree(new Solution().removeLeafNodes(buildTree([1, 3, 3, 3, 2]), 3), buildTree([1, 3, null, null, 2])))
console.log(isSameTree(new Solution().removeLeafNodes(buildTree([1, 2, null, 2, null, 2]), 2), buildTree([1])))
