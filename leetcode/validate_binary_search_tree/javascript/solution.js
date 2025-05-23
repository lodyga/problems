class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, dfs, recursion
    * @param {TreeNode} root
    * @return {number[]}
    */
   isValidBST(root) {
      return dfs(root, -Infinity, Infinity)

      function dfs(node, lowerBound, upperBound) {
         if (!node) {
            return true
         } else if (
            node.val >= upperBound ||
            node.val <= lowerBound
         ) {
            return false
         } else {
            return (
               dfs(node.left, lowerBound, node.val) &&
               dfs(node.right, node.val, upperBound)
            )
         }
      }
   };
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree, bfs, iteration, queue
    * @param {TreeNode} root
    * @return {number[]}
    */
   isValidBST(root) {
      const queue = new Queue([[root, -Infinity, Infinity]]);

      while (!queue.isEmpty()) {
         const queueSize = queue.size();

         for (let index = 0; index < queueSize; index++) {
            let [node, lowerBound, upperBound] = queue.pop();

            if (
               node.val <= lowerBound ||
               node.val >= upperBound
            ) {
               return false
            }
            if (node.left) {
               queue.push([node.left, lowerBound, Math.max(node.val, upperBound)]);
            }
            if (node.right) {
               queue.push([node.right, Math.max(node.val, lowerBound), upperBound]);
            }
         }
      }
      return true
   };
}
const isValidBST = new Solution().isValidBST;


console.log(new Solution().isValidBST(buildTree([2, 1, 3])) === true)
console.log(new Solution().isValidBST(buildTree([5, 1, 4, null, null, 3, 6])) === false)
console.log(new Solution().isValidBST(buildTree([2, 2, 2])) === false)
console.log(new Solution().isValidBST(buildTree([0, -1])) === true)
console.log(new Solution().isValidBST(buildTree([5, 4, 6, null, null, 3, 7])) === false)