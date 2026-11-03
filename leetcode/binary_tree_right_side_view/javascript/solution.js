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
    *     DS: binary tree, queue
    *     A: bfs, iteration, level-order traversal
    * @param {TreeNode} root
    * @return {number[]}
    */
   rightSideView(root) {
      if (root === null) {
         return [];
      }

      const queue = new Queue([root]);
      const res = [];

      while (!queue.isEmpty()) {
         const queueLength = queue.size();

         for (let idx = 0; idx < queueLength; idx++) {
            const node = queue.pop();

            if (idx === 0) {
               res.push(node.val);
            }

            if (node.right) {
               queue.push(node.right);
            }

            if (node.left) {
               queue.push(node.left);
            }
         }
      }

      return res;
   }
}


class Solution {
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
      
      const dfs = (node, idx) => {
         if (node === null) {
            return;
         }

         if (idx === res.length) {
            res.push(node.val);
         }

         dfs(node.right, idx + 1);
         dfs(node.left, idx + 1);
      };
      
      const res = [];
      dfs(root, 0);
      return res;
   }
}


const rightSideView = new Solution().rightSideView;
console.log(JSON.stringify(new Solution().rightSideView(buildTree([1, 2, 3]))) === JSON.stringify([1, 3]))
console.log(JSON.stringify(new Solution().rightSideView(buildTree([1, null, 3]))) === JSON.stringify([1, 3]))
console.log(JSON.stringify(new Solution().rightSideView(buildTree([1, 2, 3, null, 5, null, 4]))) === JSON.stringify([1, 3, 4]))
console.log(JSON.stringify(new Solution().rightSideView(buildTree([]))) === JSON.stringify([]))
