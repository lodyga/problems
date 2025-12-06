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
   preorderTraversal(root) {
      const nodes = [];

      const dfs = (node) => {
         if (node === null) {
            return
         }
         nodes.push(node.val);
         dfs(node.left);
         dfs(node.right);
      }
      dfs(root);
      return nodes
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: binary tree, stack, list
    *     A: dfs, iteration, pre-order traversal
    * @param {TreeNode} root
    * @return {number[]}
    */
   preorderTraversal(root) {
      const values = [];
      const stack = root ? [root] : [];

      while (stack.length) {
         const node = stack.pop();
         values.push(node.val);

         if (node.right)
            stack.push(node.right);
         if (node.left)
            stack.push(node.left);
      }
      return values
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: binary tree, stack, list
    *     A: dfs, iteration, pre-order traversal
    * @param {TreeNode} root
    * @return {number[]}
    */
   preorderTraversal(root) {
      const values = [];
      const stack = [];
      let node = root;

      while (stack.length || node) {
         if (node) {
            values.push(node.val);
            stack.push(node.right);
            node = node.left;
         } else {
            // Backtrack to the last right child
            node = stack.pop();
         }
      }
      return values
   };
}


const preorderTraversal = new Solution().preorderTraversal;
console.log(JSON.stringify(new Solution().preorderTraversal(buildTree([]))) === JSON.stringify([]))
console.log(JSON.stringify(new Solution().preorderTraversal(buildTree([1]))) === JSON.stringify([1]))
console.log(JSON.stringify(new Solution().preorderTraversal(buildTree([1, null, 2, 3]))) === JSON.stringify([1, 2, 3]))
console.log(JSON.stringify(new Solution().preorderTraversal(buildTree([1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9]))) === JSON.stringify([1, 2, 4, 5, 6, 7, 3, 8, 9]))
