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
    *     DS: binary tree, queue, list
    *     A: bfs, iteration, level-order traversal
    * @param {TreeNode} root
    * @return {number[]}
    */
   rightSideView(root) {
      if (root === null) {
         return []
      }
      const rightSideVals = [];
      const queue = new Queue([root]);

      while (queue.size()) {
         const queueLength = queue.size();

         for (let index = 0; index < queueLength; index++) {
            const node = queue.pop();

            if (index === 0) {
               rightSideVals.push(node.val);
            }
            if (node.right) {
               queue.push(node.right);
            }
            if (node.left) {
               queue.push(node.left);
            }
         }
      }
      return rightSideVals
   };

   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: 
    *     DS: binary tree, list
    *     A: dfs, recursion, pre-order traversal
    * @param {TreeNode} root
    * @return {number[]}
    */
   rightSideView(root) {
      const rightSideVals = [];

      const dfs = (index, node) => {
         if (node === null)
            return
         
         if (index === rightSideVals.length)
            rightSideVals.push(node.val)

         dfs(index + 1, node.right);
         dfs(index + 1, node.left);
      }
      dfs(0, root);
      return rightSideVals
   };
}


const rightSideView = new Solution().rightSideView;
console.log(JSON.stringify(new Solution().rightSideView(buildTree([1, 2, 3]))) === JSON.stringify([1, 3]))
console.log(JSON.stringify(new Solution().rightSideView(buildTree([1, null, 3]))) === JSON.stringify([1, 3]))
console.log(JSON.stringify(new Solution().rightSideView(buildTree([1, 2, 3, null, 5, null, 4]))) === JSON.stringify([1, 3, 4]))
console.log(JSON.stringify(new Solution().rightSideView(buildTree([]))) === JSON.stringify([]))
