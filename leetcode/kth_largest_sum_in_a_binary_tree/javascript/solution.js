import { TreeNode, buildTree, getTreeValues } from '../../../../JS/binary-tree.js';
import { Queue } from "@datastructures-js/queue";
import { MinPriorityQueue } from "@datastructures-js/priority-queue"


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
    * Tags:
    *     DS: binary tree, queue, heap
    *     A: bfs, iteration, level-order traversal
    * @param {TreeNode} root
    * @param {number} k
    * @return {number}
    */
   kthLargestLevelSum(root, k) {
      const queue = new Queue([root]);
      const minHeap = new MinPriorityQueue();

      // bfs
      while (queue.size()) {
         let levelSum = 0;
         const queueSize = queue.size();

         for (let _ = 0; _ < queueSize; _++) {
            const node = queue.dequeue();
            levelSum += node.val;

            if (node.left) {
               queue.push(node.left);
            }
            if (node.right) {
               queue.push(node.right);
            }
         }
         
         minHeap.enqueue(levelSum);
         
         if (minHeap.size() > k)
            minHeap.dequeue();
      }

      return minHeap.size() == k ? minHeap.front() : -1
   };
}


const kthLargestLevelSum = new Solution().kthLargestLevelSum;
console.log(new Solution().kthLargestLevelSum(buildTree([1, 2, null, 3]), 1) === 3)
console.log(new Solution().kthLargestLevelSum(buildTree([5, 8, 9, 2, 1, 3, 7, 4, 6]), 2) === 13)
console.log(new Solution().kthLargestLevelSum(buildTree([5, 8, 9, 2, 1, 3, 7]), 4) === -1)
