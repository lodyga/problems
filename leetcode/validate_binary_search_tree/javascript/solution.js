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
    * Tags: 
    *     DS: binary tree
    *     A: dfs, recursion, pre-order traversal
    * @param {TreeNode} root
    * @return {number[]}
    */
   isValidBST(root) {
      const dfs = (node, lowerBound, upperBound) => {
         if (node === null) {
            return true
         } else if (
            node.val >= upperBound ||
            node.val <= lowerBound
         ) {
            return false
         }
         const left = dfs(node.left, lowerBound, node.val);
         const right = dfs(node.right, node.val, upperBound);

         return left && right
      }
      return dfs(root, -(2 ** 31) - 1, 2 ** 31)
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: binary tree, queue
    *     A: bfs, iteration, level-order traversal
    * @param {TreeNode} root
    * @return {number[]}
    */
   isValidBST(root) {
      const queue = new Queue([[root, -Infinity, Infinity]]);

      while (queue.size()) {
         const [node, lowerBound, upperBound] = queue.pop();

         if (
            node.val <= lowerBound ||
            node.val >= upperBound
         ) {
            return false
         }
         if (node.left) {
            queue.push([node.left, lowerBound, node.val]);
         }
         if (node.right) {
            queue.push([node.right, node.val, upperBound]);
         }
      }
      return true
   };
}


const isValidBST = new Solution().isValidBST;
console.log(new Solution().isValidBST(buildTree([2, 1, 3])) === true)
console.log(new Solution().isValidBST(buildTree([5, 1, 4, null, null, 3, 6])) === false)
console.log(new Solution().isValidBST(buildTree([2, 2, 2])) === false)
console.log(new Solution().isValidBST(buildTree([0, -1])) === true)
console.log(new Solution().isValidBST(buildTree([5, 4, 6, null, null, 3, 7])) === false)
