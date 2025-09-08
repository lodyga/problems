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
    * Tags: binary tree, bfs, iteration, level order traversal
    * @param {TreeNode} root
    * @return {number[]}
    */
   rightSideView(root) {
      const queue = new Queue([root]);
      const rightSideViewValues = [];

      while (!queue.isEmpty()) {
         let levelView = null;
         const queueLength = queue.size();

         for (let index = 0; index < queueLength; index++) {
            let node = queue.pop();

            if (node) {
               if (!levelView) {
                  levelView = node.val;
               }
               queue.push(node.right);
               queue.push(node.left);
            }
         }
         if (levelView) {
            rightSideViewValues.push(levelView);
         }
      }
      return rightSideViewValues
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
   rightSideView(root) {
      const rightSideViewValues = [];
      dfs(0, root);
      return rightSideViewValues

      function dfs(index, node) {
         if (!node) 
            return
         else if (index === rightSideViewValues.length)
            rightSideViewValues.push(node.val)

         dfs(index + 1, node.right);
         dfs(index + 1, node.left);
      }

   };
}
const rightSideView = new Solution().rightSideView;


console.log(new Solution().rightSideView(buildTree([1, 2, 3])), [1, 3])
console.log(new Solution().rightSideView(buildTree([1, null, 3])), [1, 3])
console.log(new Solution().rightSideView(buildTree([1, 2, 3, null, 5, null, 4])), [1, 3, 4])
console.log(new Solution().rightSideView(buildTree([])), []