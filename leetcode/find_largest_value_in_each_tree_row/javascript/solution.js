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
    * Tags: binary tree, bfs, iteration, queue, level order traversal
    * @param {TreeNode} root
    * @return {number[]}
    */
   largestValues(root) {
      const values = [];

      const bfs = (node) => {
         const queue = new Queue();
         if (node)
            queue.enqueue(node);

         while (!queue.isEmpty()) {
            const queue_size = queue.size();
            for (let index = 0; index < queue_size; index++) {
               const node = queue.dequeue();

               if (index === 0)
                  values.push(node.val);
               else {
                  if (node.val > values[values.length - 1])
                     values[values.length - 1] = node.val;
               }

               if (node.left)
                  queue.enqueue(node.left);
               if (node.right)
                  queue.enqueue(node.right);

            }
         }
      };
      bfs(root)
      return values
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, dfs, recursion, level order traversal
    * @param {TreeNode} root
    * @return {number[]}
    */
   largestValues(root) {
      const values = [];

      const dfs = (index, node) => {
         if (!node)
            return
         else if (values.length === index)
            values.push(node.val);
         else if (node.val > values[index])
            values[index] = node.val;

         dfs(index + 1, node.left)
         dfs(index + 1, node.right)
      };
      dfs(0, root);
      return values
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, dfs, iteration, stack
    * @param {TreeNode} root
    * @return {number[]}
    */
   largestValues(root) {
      const values = [];
      const stack = [];

      const dfs = (node) => {
         if (node)
            stack.push([0, node]);

         while (stack.length) {
            const [index, node] = stack.pop();

            if (index === values.length)
               values.push(node.val);
            else if (node.val > values[index])
               values[index] = node.val

            if (node.right)
               stack.push([index + 1, node.right]);
            if (node.left)
               stack.push([index + 1, node.left]);
         }
      };
      dfs(root);
      return values
   };
}


const largestValues = new Solution().largestValues;
console.log(new Solution().largestValues(buildTree([1, 3, 2, 5, 3, null, 9])), [1, 3, 9])
console.log(new Solution().largestValues(buildTree([1, 2, 3])), [1, 3])
console.log(new Solution().largestValues(buildTree([])), [])
console.log(new Solution().largestValues(buildTree([3, 1, 5, 0, 2, 4, 6])), [3, 5, 6])