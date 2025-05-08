class ListNode {
   constructor(val = null, next = null) {
      this.val = val
      this.next = next
   };
}


class MyHashSet {
   /**
    * Time complexity:
    *     constructor: O(n)
    *     add: O(1)
    *     contains: O(1)
    *     remove: O(1)
    * Auxiliary space complexity: O(n)
    * Tags: linked list, hash set
    */
   constructor() {
      this.bucketSize = 10 ** 4;
      this.bucket = Array.from({ length: this.bucketSize }, () => new ListNode());
   };

   /**
    * @param {number} key 
    * @returns {void}
    */
   add(key) {
      const index = this.getHashCode(key);
      let node = this.bucket[index];

      while (node.next) {
         if (node.next.val == key)
            return
         node = node.next;
      }
      node.next = new ListNode(key);
   };

   /**
    * @param {number} key 
    * @returns {boolean}
    */
   contains(key) {
      const index = this.getHashCode(key);
      let node = this.bucket[index];

      while (node.next) {
         if (node.next.val == key)
            return true
         else
            node = node.next;
      }
      return false
   };

   /**
    * @param {number} key 
    * @returns {void}
    */
   remove(key) {
      const index = this.getHashCode(key);
      let node = this.bucket[index];

      while (node.next) {
         if (node.next.val == key) {
            node.next = node.next.next;
            return
         }
         else
            node = node.next;
      }
   };

   /**
    * @param {number} key 
    * @returns {number}
    */
   getHashCode(key) {
      return key % this.bucketSize
   };
}


const myHashSet = new MyHashSet();
myHashSet.add(1)  // set = [1]
myHashSet.add(2)  // set = [1, 2]
console.log(myHashSet.contains(1))  // return True
console.log(myHashSet.contains(3))  // return False, (not found)
myHashSet.add(2)  // set = [1, 2]
console.log(myHashSet.contains(2))  // return True
myHashSet.remove(2)  // set = [1]
console.log(myHashSet.contains(2))  // return False, (already removed)