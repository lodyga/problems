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
      const res = [];

      const dfs = (node) => {
         if (node === null) {
            return
         }

         dfs(node.left);
         dfs(node.right);
         res.push(node.val);
      }

      dfs(root);
      return res;
   }
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: binary tree, stack
    *     A: dfs, iteration, pre-order traversal
    * @param {TreeNode} root
    * @return {number[]}
    */
   postorderTraversal(root) {
      const res = [];
      const stack = [];
      let node = root;

      while (node || stack.length) {
         if (node) {
            res.push(node.val);
            stack.push(node);
            node = node.right;
         } else {
            // Backtrack to the last right child
            node = stack.pop();
            node = node.left;
         }
      }
      
      res.reverse();
      return res;
   }
}


const postorderTraversal = new Solution().postorderTraversal;
console.log(JSON.stringify(new Solution().postorderTraversal(buildTree([]))) === JSON.stringify([]))
console.log(JSON.stringify(new Solution().postorderTraversal(buildTree([1]))) === JSON.stringify([1]))
console.log(JSON.stringify(new Solution().postorderTraversal(buildTree([1, null, 2, 3]))) === JSON.stringify([3, 2, 1]))
console.log(JSON.stringify(new Solution().postorderTraversal(buildTree([1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9]))) === JSON.stringify([4, 6, 7, 5, 2, 9, 8, 3, 1]))
