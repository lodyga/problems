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
    * @param {number} val
    * @return {TreeNode}
    */
   insertIntoBST(root, val) {
      return dfs(root)

      function dfs(node) {
         if (!node) {
            node = new TreeNode(val)
         } else if (node.val < val) {
            node.right = dfs(node.right);
         } else {
            node.left = dfs(node.left);
         }
         return node
      }
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: binary tree, bfs, iteration
    * @param {TreeNode} root
    * @param {number} val
    * @return {TreeNode}
    */
   insertIntoBST(root, val) {
      if (!root) {
         return new TreeNode(val)
      }
      let node = root;

      while (node) {
         if (node.val < val) {
            if (node.right) {
               node = node.right;
            } else {
               node.right = new TreeNode(val);
               return root
            }
         } else {
            if (node.left) {
               node = node.left;
            } else {
               node.left = new TreeNode(val);
               return root
            }
         }
      }
   };
}
const insertIntoBST = new Solution().insertIntoBST;


console.log(getTreeValues(new Solution().insertIntoBST(buildTree([5]), 6)), [5, null, 6])
console.log(getTreeValues(new Solution().insertIntoBST(buildTree([]), 5)), [5])
console.log(getTreeValues(new Solution().insertIntoBST(buildTree([4, 2, 7, 1, 3]), 5)), [4, 2, 7, 1, 3, 5])
console.log(getTreeValues(new Solution().insertIntoBST(buildTree([40, 20, 60, 10, 30, 50, 70]), 25)), [40, 20, 60, 10, 30, 50, 70, null, null, 25])
console.log(getTreeValues(new Solution().insertIntoBST(buildTree([4, 2, 7, 1, 3, null, null, null, null, null, null]), 5)), [4, 2, 7, 1, 3, 5])