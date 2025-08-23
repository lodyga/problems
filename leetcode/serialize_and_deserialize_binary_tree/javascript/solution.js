// import { buildTree, getTreeValues, TreeNode } from 'file:///home/ukasz/Documents/IT/JS/binary-tree.js';
import { buildTree, getTreeValues, TreeNode } from '../../../../JS/binary-tree.js';


/**
 * Time complexity: O(n)
 * Auxiliary space complexity: O(n)
 * Tags: binary tree, dfs, recursion, pre-order traversal
 */
class Codec {
   /**
    * @param {TreeNode} root
    * @returns {string}
    */
   serialize(root) {
      const values = [];

      const dfs = (node) => {
         if (!node) {
            values.push('null')
            return
         }
         values.push((node.val).toString());
         dfs(node.left);
         dfs(node.right);
      };
      dfs(root);
      return values.join(',')
   };

   /**
    * @param {string} data
    * @returns {TreeNode}
    */
   deserialize(data) {
      let values = data.split(',');
      let index = 0;

      const dfs = () => {
         if (values[index] === 'null') {
            index++;
            return null
         }

         const node = new TreeNode(parseInt(values[index]));
         index++;
         node.left = dfs();
         node.right = dfs();
         return node
      }
      return dfs()
   };
}
const serialize = new Codec().serialize;
const deserialize = new Codec().deserialize;

//console.log(new Codec().serialize(buildTree([1, 2, 3, null, null, 4, 5])))
//console.log(new Codec().deserialize(new Codec().serialize(buildTree([1, 2, 3, null, null, 4, 5]))))
console.log(getTreeValues(new Codec().deserialize(new Codec().serialize(buildTree([1, 2, 3, null, null, 4, 5])))), [1, 2, 3, null, null, 4, 5])