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
    *     side effect
    * @param {TreeNode} root
    * @return {number[]}
    */
   goodNodes(root) {
      let res = 0;

      const dfs = (node, maxVal) => {
         if (node === null) return

         maxVal = Math.max(maxVal, node.val);
         res += node.val >= maxVal ? 1 : 0;
         dfs(node.left, maxVal);
         dfs(node.right, maxVal);
      }

      dfs(root, root.val)
      return res
   }
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: binary tree
    *     A: dfs, recursion, pre-order traversal
    *     pure function
    * @param {TreeNode} root
    * @return {number[]}
    */
   goodNodes(root) {
      const dfs = (node, maxVal) => {
         if (node === null) {
            return 0
         }

         maxVal = Math.max(maxVal, node.val);
         const isGood = node.val >= maxVal;
         const left = dfs(node.left, maxVal);
         const right = dfs(node.right, maxVal);
         return isGood + left + right
      }

      return dfs(root, root.val)
   }
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: binary tree, stack
    *     A: dfs, iteration, pre-order traversal
    * @param {TreeNode} root
    * @return {number[]}
    */
   goodNodes(root) {
      const stack = [[root, root.val]];
      let res = 0;

      while (stack.length) {
         let [node, maxVal] = stack.pop();
         maxVal = Math.max(maxVal, node.val);
         res += node.val >= maxVal ? 1 : 0;

         if (node.left)
            stack.push([node.left, maxVal]);
         if (node.right)
            stack.push([node.right, maxVal]);
      }
      return res
   }
}


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
   goodNodes(root) {
      const queue = new Queue([[root, root.val]]);
      let res = 0;

      while (queue.size()) {
         let [node, maxVal] = queue.pop();
         maxVal = Math.max(maxVal, node.val);
         res += node.val >= maxVal ? 1 : 0;

         if (node.left)
            queue.push([node.left, maxVal]);
         if (node.right)
            queue.push([node.right, maxVal]);
      }
      return res
   }
}


const goodNodes = new Solution().goodNodes;
console.log(new Solution().goodNodes(buildTree([1])) === 1)
console.log(new Solution().goodNodes(buildTree([1, 2, 3])) === 3)
console.log(new Solution().goodNodes(buildTree([3, 1, 4, 3, null, 1, 5])) === 4)
console.log(new Solution().goodNodes(buildTree([3, 3, null, 4, 2])) === 3)
