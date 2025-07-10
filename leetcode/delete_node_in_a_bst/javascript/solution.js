class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary tree
    * @param {TreeNode} root
    * @param {number} key
    * @return {TreeNode}
   */
   deleteNode(root, key) {
      const dfs = (node) => {
         if (!node) {
            return node
         }
         else if (key == node.val) {
            if (!node.right) {
               node = node.left;
            } else if (!node.left) {
               node = node.right;
            } else {
               let bottom_node = node.right;
               while (bottom_node.left) {
                  bottom_node = bottom_node.left;
               }
               node.val = bottom_node.val;
               node.right = this.deleteNode(node.right, node.val)
            }
         }
         else if (key < node.val) {
            node.left = dfs(node.left)
         }
         else {
            node.right = dfs(node.right)
         }
         return node
      }
      
      return dfs(root)
   };
}
// Bind the method to the instance
const solution = new Solution();
const deleteNode = solution.deleteNode.bind(solution); // Bind the context

// static method
// const deleteNode = Solution.deleteNode;


console.log(getTreeValues(new Solution().deleteNode(buildTree([5, 3, 6]), 6)), [5, 3])
console.log(getTreeValues(new Solution().deleteNode(buildTree([5, 3, 6]), 3)), [5, null, 6])
console.log(getTreeValues(new Solution().deleteNode(buildTree([5, 3, 6]), 5)), [6, 3])
console.log(getTreeValues(new Solution().deleteNode(buildTree([5, 3, 6, 2, 4, null, 7]), 3)), [5, 4, 6, 2, null, null, 7])
console.log(getTreeValues(new Solution().deleteNode(buildTree([5, 3, 6, 2, 4, null, 7]), 0)), [5, 3, 6, 2, 4, null, 7])
console.log(getTreeValues(new Solution().deleteNode(buildTree([]), 0)), [])
console.log(getTreeValues(new Solution().deleteNode(buildTree([0]), 0)), [])