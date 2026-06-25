/**
 * Time complexity: O(1)
 * Auxiliary space complexity: O(n)
 * Tags:
 *     DS: list, string
 *     A: iterator
 */
class StringIterator {
   constructor(text) {
      this.text = text;
      this.idx = 0;
      this.counter = 0;
      this._findNext();
   }

   /**
    * @param {}
    * @return {void}
    */
   _findNext() {
      if (this.counter) {
         this.counter--;
         return;
      }

      while (this.idx < this.text.length) {
         this.nextLetter = this.text[this.idx];
         this.idx++;
         this.counter = 0;

         while (
            this.idx < this.text.length
            && '0' <= this.text[this.idx]
            && this.text[this.idx] <= '9'
         ) {
            this.counter = this.counter * 10 + Number(this.text[this.idx]);
            this.idx++;
         }

         if (this.counter === 0) {
            continue;
         }

         this.counter--;
         return;
      }

      this.nextLetter = ' ';
   }

   /**
    * @param {}
    * @return {string}
    */
   next() {
      const res = this.nextLetter;
      this._findNext();
      return res;
   }

   /**
    * @param {}
    * @return {boolean}
    */
   hasNext() {
      return this.nextLetter !== ' ';
   }
}


const iterator = new StringIterator('L1e2t1C1o1d1e1')
console.log(iterator.next() == 'L')
console.log(iterator.next() == 'e')
console.log(iterator.next() == 'e')
console.log(iterator.next() == 't')
console.log(iterator.next() == 'C')
console.log(iterator.next() == 'o')
console.log(iterator.next() == 'd')
console.log(iterator.hasNext() === true)
console.log(iterator.next() === 'e')
console.log(iterator.hasNext() == false)
console.log(iterator.next() === ' ')
