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
    * @return {number[]}
    */
   inorderTraversal(root) {
      const values = [];

      const dfs = (node) => {
         if (node === null) {
            return
         }
         dfs(node.left);
         values.push(node.val);
         dfs(node.right);
      }
      dfs(root);
      return values
   };


   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: binary tree, stack
    *     A: dfs, iteration, pre-order traversal
    * @param {TreeNode} root
    * @return {number[]}
    */
   inorderTraversal(root) {
      const values = [];
      const stack = [];
      let node = root;

      while (node || stack.length) {
         if (node) {
            stack.push(node);
            node = node.left;
         } else {
            node = stack.pop();
            values.push(node.val);
            node = node.right;
         }
      }
      return values
   };
}


const inorderTraversal = new Solution().inorderTraversal;
console.log(JSON.stringify(new Solution().inorderTraversal(buildTree([]))) === JSON.stringify([]))
console.log(JSON.stringify(new Solution().inorderTraversal(buildTree([1]))) === JSON.stringify([1]))
console.log(JSON.stringify(new Solution().inorderTraversal(buildTree([1, null, 2, 3]))) === JSON.stringify([1, 3, 2]))
console.log(JSON.stringify(new Solution().inorderTraversal(buildTree([1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9]))) === JSON.stringify([4, 2, 6, 5, 7, 1, 3, 9, 8]))
