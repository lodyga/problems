import { Queue } from "@datastructures-js/queue";


/**
 * // Definition for a _Node.
 * function _Node(val, left, right, next) {
 *    this.val = val === undefined ? null : val;
 *    this.left = left === undefined ? null : left;
 *    this.right = right === undefined ? null : right;
 *    this.next = next === undefined ? null : next;
 * };
 */


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: binary tree, queue
    *     A: bfs, iteration, level-order traversal
    * @param {_Node} root
    * @return {_Node}
    */
   connect(root) {
      if (root === null) {
         return null
      }

      const queue = new Queue([root]);

      // bfs
      while (queue.size()) {
         const queueSize = queue.size();
         let nodeNext = null;

         if (queue.front() === null) {
            break
         }

         for (let _ = 0; _ < queueSize; _++) {
            const node = queue.dequeue();
            node.next = nodeNext;
            nodeNext = node;
            queue.enqueue(node.right);
            queue.enqueue(node.left);
         }
      }

      return root
   }
};