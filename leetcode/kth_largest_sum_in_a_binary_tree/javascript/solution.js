import { TreeNode, buildTree, getTreeValues } from '../../../../JS/binary-tree.js';
import { MinPriorityQueue } from "@datastructures-js/priority-queue"
import { Queue } from "@datastructures-js/queue";


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
    * Time complexity: O(nlogk)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, bfs, iteration, queue, level order traversal
    * @param {TreeNode} root
    * @param {number} k
    * @return {number}
    */
   kthLargestLevelSum(root, k) {
      // minHeap.size() === k at most
      const minHeap = new MinPriorityQueue();

      const bfs = (node) => {
         const queue = new Queue([node]);

         while (!queue.isEmpty()) {
            let levelSum = 0;
            const queue_size = queue.size();

            for (let index = 0; index < queue_size; index++) {
               const node = queue.pop();
               levelSum += node.val;

               if (node.left)
                  queue.push(node.left);
               if (node.right)
                  queue.push(node.right);
            }
            minHeap.enqueue(levelSum);
            if (minHeap.size() > k)
               minHeap.dequeue();
         }
      }

      bfs(root)
      return minHeap.size() == k ? minHeap.front() : -1
   };
}


const kthLargestLevelSum = new Solution().kthLargestLevelSum;
console.log(new Solution().kthLargestLevelSum(buildTree([1, 2, null, 3]), 1) === 3)
console.log(new Solution().kthLargestLevelSum(buildTree([5, 8, 9, 2, 1, 3, 7, 4, 6]), 2) === 13)
