class ListNode {
   constructor(key = null, val = null, next = null) {
      this.key = key;
      this.val = val;
      this.next = next;
   }
}


class MyHashMap {
   /**
    * Time complexity: 
    *     put: O(1)
    *     get: O(1)
    *     remove: O(1)
    * Auxiliary space complexity: O(n)
    * Tags: linked list, hash map
    * @param {}
    * @return {}
    */

   constructor() {
      this.bucketSize = 10 ** 4;
      this.buckets = Array.from({ length: this.bucketSize }, () => new ListNode());
   };

   /**
    * @param {number} key 
    * @param {number} val 
    * @returns {void}
    */
   put(key, val) {
      const index = this.getHashCode(key);
      let node = this.buckets[index];

      while (node.next) {
         if (node.next.key === key) {
            node.next.val = val;
            return
         } else
            node = node.next;
      }
      node.next = new ListNode(key, val);
   };

   /**
    * @param {number} key 
    * @returns {number}
    */
   get(key) {
      const index = this.getHashCode(key);
      let node = this.buckets[index].next;

      while (node) {
         if (node.key === key) {
            return node.val
         } else
            node = node.next;
      }
      return -1
   };

   /**
    * @param {number} key 
    * @returns {void}
    */
   remove(key) {
      const index = this.getHashCode(key);
      let node = this.buckets[index];

      while (node.next) {
         if (node.next.key === key) {
            node.next = node.next.next;
            return
         } else
            node = node.next;
      }
   };

   /**
    * @param {number} key 
    * @returns {number}
    */
   getHashCode(key) {
      return key % this.bucketSize;
   }
}


const myHashMap = new MyHashMap()
myHashMap.put(1, 1)  // The map is now[[1, 1]]
myHashMap.put(2, 2)  // The map is now[[1, 1], [2, 2]]
console.log(myHashMap.get(1))  // return 1, The map is now[[1, 1], [2, 2]]
console.log(myHashMap.get(3))  // return -1(i.e., not found), The map is now[[1, 1], [2, 2]]
myHashMap.put(2, 1)  // The map is now[[1, 1], [2, 1]]
console.log(myHashMap.get(2))  // return 1, The map is now[[1, 1], [2, 1]]
myHashMap.remove(2)  // remove the mapping for 2, The map is now[[1, 1]]
console.log(myHashMap.get(2))  // return -1(i.e., not found), The map is now[[1, 1]]