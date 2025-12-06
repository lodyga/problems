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
    * @param {number} targetSum
    * @return {boolean}
    */
   hasPathSum(root, targetSum) {
      return dfs(root, targetSum)

      function dfs(node, targetSum) {
         if (node === null) {
            return false
         } else if (
            !node.left && !node.right
         ) {
            return targetSum - node.val === 0
         } else {
            return (
               dfs(node.left, targetSum - node.val) ||
               dfs(node.right, targetSum - node.val)
            )
         }
      }
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, dfs, iteration, stack
    * @param {TreeNode} root
    * @param {number} targetSum
    * @return {boolean}
    */
   hasPathSum(root, targetSum) {
      if (root === null) return false
      const stack = [[root, targetSum]];

      while (stack.length) {
         const [node, targetSum] = stack.pop();

         if (
            !node.left &&
            !node.right &&
            targetSum - node.val === 0   
         ) return true
         if (node.right) 
            stack.push([node.right, targetSum - node.val]);
         if (node.left) 
            stack.push([node.left, targetSum - node.val]);
      }
      return false
   };
}

class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, bfs, iteration, queue
    * @param {TreeNode} root
    * @param {number} targetSum
    * @return {boolean}
    */
   hasPathSum(root, targetSum) {
      if (root === null) return false
      const queue = new Queue([[root, targetSum]])



      while (!queue.isEmpty()) {
         const [node, targetSum] = queue.pop();

         if (
            !node.left &&
            !node.right &&
            targetSum - node.val === 0   
         ) return true
         if (node.right) 
            queue.push([node.right, targetSum - node.val]);
         if (node.left) 
            queue.push([node.left, targetSum - node.val]);
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