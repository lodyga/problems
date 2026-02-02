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
   largestValues(root) {
      const res = [];

      const bfs = (node) => {
         const queue = new Queue();
         if (node)
            queue.enqueue(node);

         while (queue.size()) {
            res.push(queue.front().val);
            const queue_size = queue.size();

            for (let index = 0; index < queue_size; index++) {
               const node = queue.dequeue();

               res[res.length - 1] = Math.max(res[res.length - 1], node.val)

               if (node.left)
                  queue.enqueue(node.left);
               if (node.right)
                  queue.enqueue(node.right);

            }
         }
      };
      bfs(root)
      return res
   };


   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: binary tree, list
    *     A: dfs, recursion, level-order traversal
    * @param {TreeNode} root
    * @return {number[]}
    */
   alargestValues(root) {
      const res = [];

      const dfs = (index, node) => {
         if (!node)
            return
         else if (res.length === index)
            res.push(node.val);
         else if (node.val > res[index])
            res[index] = node.val;

         dfs(index + 1, node.left)
         dfs(index + 1, node.right)
      };
      dfs(0, root);
      return res
   };


   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: binary tree, list, stack
    *     A: dfs, iteration, level-order traversal
    * @param {TreeNode} root
    * @return {number[]}
    */
   clargestValues(root) {
      const res = [];
      const stack = [];

      const dfs = (node) => {
         if (node)
            stack.push([0, node]);

         while (stack.length) {
            const [index, node] = stack.pop();

            if (index === res.length)
               res.push(node.val);
            else if (node.val > res[index])
               res[index] = node.val

            if (node.right)
               stack.push([index + 1, node.right]);
            if (node.left)
               stack.push([index + 1, node.left]);
         }
      };
      dfs(root);
      return res
   };
}


const largestValues = new Solution().largestValues;
console.log(new Solution().largestValues(buildTree([1, 3, 2, 5, 3, null, 9])).toString() === [1, 3, 9].toString())
console.log(new Solution().largestValues(buildTree([1, 2, 3])).toString() === [1, 3].toString())
console.log(new Solution().largestValues(buildTree([])).toString() === [].toString())
console.log(new Solution().largestValues(buildTree([3, 1, 5, 0, 2, 4, 6])).toString() === [3, 5, 6].toString())
console.log(new Solution().largestValues(buildTree([34, -6, null, -21])).toString() === [34, -6, -21].toString())
