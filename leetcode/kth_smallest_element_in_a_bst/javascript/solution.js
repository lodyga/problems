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
    *     A: dfs, recursion, in-order traversal
    * @param {TreeNode} root
    * @param {number} k
    * @return {number}
    */
   kthSmallest(root, k) {
      const values = [];
      
      const dfs = (node, k) => {
         if (node === null) {
            return
         }

         dfs(node.left);

         values.push(node.val);
         if (values.length === k)
            return

         dfs(node.right);
      }
      dfs(root);
      return values[k - 1]
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: binary tree, stack
    *     A: dfs, iteration, in-order traversal
    * @param {TreeNode} root
    * @param {number} k
    * @return {number}
    */
   kthSmallest(root, k) {
      const values = [];
      const stack = [];
      let node = root;

      while (node || stack) {
         if (node) {
            stack.push(node);
            node = node.left;
         } else {
            node = stack.pop();
            values.push(node.val);
            if (values.length === k)
               return values[values.length - 1]
            node = node.right;
         }
      }
   };
}


const kthSmallest = new Solution().kthSmallest;
console.log(new Solution().kthSmallest(buildTree([1]), 1) === 1)
console.log(new Solution().kthSmallest(buildTree([2, 1, 3]), 1) === 1)
console.log(new Solution().kthSmallest(buildTree([1, null, 2]), 2) === 2)
console.log(new Solution().kthSmallest(buildTree([5, 3, 6, 2, 4, null, null, 1]), 3) === 3)
console.log(new Solution().kthSmallest(buildTree([5, 3, 7, 2, 4, null, 8]), 3) === 4)
console.log(new Solution().kthSmallest(buildTree([3, 1, 4, null, 2]), 1) === 1)
console.log(new Solution().kthSmallest(buildTree([41, 37, 44, 24, 39, 42, 48, 1, 35, 38, 40, null, 43, 46, 49, 0, 2, 30, 36, null, null, null, null, null, null, 45, 47, null, null, null, null, null, 4, 29, 32, null, null, null, null, null, null, 3, 9, 26, null, 31, 34, null, null, 7, 11, 25, 27, null, null, 33, null, 6, 8, 10, 16, null, null, null, 28, null, null, 5, null, null, null, null, null, 15, 19, null, null, null, null, 12, null, 18, 20, null, 13, 17, null, null, 22, null, 14, null, null, 21, 23]), 25) === 24)
