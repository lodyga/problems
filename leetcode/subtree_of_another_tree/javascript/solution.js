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
    * Tags: 
    *     DS: binary tree
    *     A: dfs, recursion, pre-order traversal
    * @param {TreeNode} root
    * @param {TreeNode} subRoot
    * @return {boolean}
    */
   isSubtree(root, subRoot) {
      const isSameTree = (node1, node2) => {
         if (node1 === null && node2 === null) {
            return true
         } else if (node1 === null || node2 === null) {
            return false
         } else if (node1.val !== node2.val) {
            return false
         }
         const left = isSameTree(node1.left, node2.left);
         const right = isSameTree(node1.right, node2.right);

         return left && right
      }

      if (subRoot === null) {
         return true
      } else if (root === null) {
         return false
      }

      const dfs = (node) => {
         if (node === null) {
            return false
         }
         else if (isSameTree(node, subRoot)) {
            return true
         }

         const left = dfs(node.left);
         const right = dfs(node.right);

         return left || right
      }
      return dfs(root)
   };
}


const isSubtree = new Solution().isSubtree;
console.log(new Solution().isSubtree(buildTree([3, 4, 5, 1, 2]), buildTree([4, 1, 2])) === true)
console.log(new Solution().isSubtree(buildTree([3, 4, 5, 1, 2, null, null, null, null, 0]), buildTree([4, 1, 2])) === false)
console.log(new Solution().isSubtree(buildTree([1, null, 1, null, 1, null, 1, null, 1, null, 1, null, 1, null, 1, null, 1, null, 1, null, 1, 2]), buildTree([1, null, 1, null, 1, null, 1, null, 1, null, 1, 2])) == true)
