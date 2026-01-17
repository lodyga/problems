import { TreeNode, buildTree, getTreeValues } from '../../../../JS/binary-tree.js';
import { Queue } from '@datastructures-js/queue';


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
    * @param {number} targetSum
    * @return {boolean}
    */
   hasPathSum(root, targetSum) {
      const dfs = (node, total) => {
         if (node === null) {
            return false
         } else if (
            node.left === null && node.right === null
         ) {
            return total + node.val === targetSum
         }
         const left = dfs(node.left, total + node.val);
         const right = dfs(node.right, total + node.val);
         return left || right
      }
      return dfs(root, 0)
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: binary tree, stack
    *     A: dfs, iteration, pre-order traversal
    * @param {TreeNode} root
    * @param {number} targetSum
    * @return {boolean}
    */
   hasPathSum(root, targetSum) {
      if (root === null)
         return false
      const stack = [[root, 0]];

      while (stack.length) {
         const [node, pathSum] = stack.pop();

         if (
            node.left === null &&
            node.right === null &&
            pathSum + node.val === targetSum
         ) return true
         
         if (node.right)
            stack.push([node.right, pathSum + node.val]);
         if (node.left)
            stack.push([node.left, pathSum + node.val]);
      }
      return false
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, bfs, iteration, queue
    * @param {TreeNode} root
    * @param {number} targetSum
    * @return {boolean}
    */
   hasPathSum(root, targetSum) {
      if (root === null) {
         return false
      }
      const queue = new Queue([[root, 0]]);

      while (queue.size()) {
         const [node, pathSum] = queue.pop();

         if (
            node.left === null &&
            node.right === null &&
            pathSum + node.val === targetSum
         ) return true
         
         if (node.left)
            queue.push([node.left, pathSum + node.val]);
         if (node.right)
            queue.push([node.right, pathSum + node.val]);
      }
      return false
   };
}


const hasPathSum = new Solution().hasPathSum;
console.log(new Solution().hasPathSum(buildTree([5]), 5) === true)
console.log(new Solution().hasPathSum(buildTree([5, 4, 3]), 8) === true)
console.log(new Solution().hasPathSum(buildTree([5, 4, 3]), 11) === false)
console.log(new Solution().hasPathSum(buildTree([1, 2]), 1) === false)
console.log(new Solution().hasPathSum(buildTree([5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1]), 22) === true)
console.log(new Solution().hasPathSum(buildTree([1, 2, 3]), 5) === false)
console.log(new Solution().hasPathSum(buildTree([]), 0) === false)
