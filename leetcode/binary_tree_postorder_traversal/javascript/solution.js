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
   postorderTraversal(root) {
      const nodes = [];

      const dfs = (node) => {
         if (node === null) {
            return
         }
         dfs(node.left);
         dfs(node.right);
         nodes.push(node.val);
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
   postorderTraversal(root) {
      const nodes = [];
      const stack = [];
      let node = root;

      while (node || stack.length) {
         if (node) {
            nodes.push(node.val);
            stack.push(node);
            node = node.right;
         } else {
            // Backtrack to the last right child
            node = stack.pop();
            node = node.left;
         }
      }
      nodes.reverse();
      return nodes
   };
}


const postorderTraversal = new Solution().postorderTraversal;
console.log(JSON.stringify(new Solution().postorderTraversal(buildTree([]))) === JSON.stringify([]))
console.log(JSON.stringify(new Solution().postorderTraversal(buildTree([1]))) === JSON.stringify([1]))
console.log(JSON.stringify(new Solution().postorderTraversal(buildTree([1, null, 2, 3]))) === JSON.stringify([3, 2, 1]))
console.log(JSON.stringify(new Solution().postorderTraversal(buildTree([1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9]))) === JSON.stringify([4, 6, 7, 5, 2, 9, 8, 3, 1]))
