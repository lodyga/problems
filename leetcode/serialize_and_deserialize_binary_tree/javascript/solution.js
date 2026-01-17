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


/**
 * Time complexity: O(n)
 * Auxiliary space complexity: O(n)
 * Tags:
 *     DS: binary tree, queue
 *     A: bfs, iteration, level-order traversal
 */
class Codec {
   /**
    * @param {TreeNode} root
    * @returns {string}
    */
   serialize(root) {
      if (root === null)
         return ''

      const res = [];
      const queue = new Queue([root]);

      while (queue.size()) {
         const node = queue.dequeue();

         if (node) {
            res.push(node.val.toString());
            queue.enqueue(node.left);
            queue.enqueue(node.right);
         } else {
            res.push('null');
         }
      }

      while (res && res[res.length - 1] === 'null')
         res.pop();

      return res.join(',')
   };

   /**
    * @param {string} data
    * @returns {TreeNode}
    */
   deserialize(data) {
      if (data === '')
         return null

      const nodes = data.split(',');
      let val = nodes[0];
      const root = new TreeNode(Number(val));
      const queue = new Queue([root]);
      let index = 1;

      while (index < nodes.length) {
         const node = queue.dequeue();

         val = nodes[index];
         node.left = val === 'null' ? null : new TreeNode(Number(val));
         if (node.left)
            queue.enqueue(node.left);
         index += 1;

         if (index === nodes.length)
            break

         val = nodes[index];
         node.right = val === 'null' ? null : new TreeNode(Number(val));
         if (node.right)
            queue.enqueue(node.right);
         index += 1;
      }

      return root
   };

}


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
         if (node === null) {
            values.push('null')
            return
         }
         values.push((node.val).toString());
         dfs(node.left);
         dfs(node.right);
      };
      dfs(root);
      return values.join('','')
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

         const node = new TreeNode(Math.floor(values[index]));
         index++;
         node.left = dfs();
         node.right = dfs();
         return node
      }
      return dfs()
   };
}


console.log(getTreeValues(new Codec().deserialize(new Codec().serialize(buildTree([4])))).toString() === [4].toString())
console.log(getTreeValues(new Codec().deserialize(new Codec().serialize(buildTree([4, 5, 6])))).toString() === [4, 5, 6].toString())
console.log(getTreeValues(new Codec().deserialize(new Codec().serialize(buildTree([4, 5])))).toString() === [4, 5].toString())
console.log(getTreeValues(new Codec().deserialize(new Codec().serialize(buildTree([4, null, 6])))).toString() === [4, null, 6].toString())
console.log(getTreeValues(new Codec().deserialize(new Codec().serialize(buildTree([])))).toString() === [].toString())
console.log(getTreeValues(new Codec().deserialize(new Codec().serialize(buildTree([1, 2, 3, null, null, 4, 5])))).toString() === [1, 2, 3, null, null, 4, 5].toString())
console.log(getTreeValues(new Codec().deserialize(new Codec().serialize(buildTree([1, 2, 3, null, null, 4, 5, 6, 7])))).toString() === [1, 2, 3, null, null, 4, 5, 6, 7].toString())
