import { TreeNode, buildTree, getTreeValues, isSameTree } from '../../../../JS/binary-tree.js';


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
    * @param {number[]} nums
    * @return {TreeNode}
    */
   sortedArrayToBST(nums) {
      const dfs = (left, right) => {
         if (left === right) {
            return new TreeNode(nums[left])
         }
         else if (left > right) {
            return null
         }

         const middle = (left + right) >> 1;
         const node = new TreeNode(nums[middle]);
         node.left = dfs(left, middle - 1);
         node.right = dfs(middle + 1, right);
         return node
      }
      return dfs(0, nums.length - 1)
   };
}


const sortedArrayToBST = new Solution().sortedArrayToBST;
console.log(isSameTree(new Solution().sortedArrayToBST([5]), buildTree([5])))
console.log(isSameTree(new Solution().sortedArrayToBST([1, 3]), buildTree([1, null, 3])))
console.log(isSameTree(new Solution().sortedArrayToBST([-10, -3, 0, 5, 9]), buildTree([0, -10, 5, null, -3, null, 9])))
