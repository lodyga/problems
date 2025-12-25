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
      this.index = 0;
      this.letter = '';
      this.letterCounter = 0;
   };

   /**
    * @param {}
    * @return {}
    */
   _getNextLetter() {
      this.letter = this.text[this.index];
      this.index += 1;

      let multi = 0;
      while (
         this.index < this.text.length &&
         '0' <= this.text[this.index] &&
         this.text[this.index] <= '9'
      ) {
         multi = multi * 10 + Number(this.text[this.index]);
         this.index += 1;
      }
      this.letterCounter = multi - 1;

      return this.letter
   };

   /**
    * @param {}
    * @return {string}
    */
   next() {
      if (this.letterCounter) {
         const nextLetter = this.letter;
         this.letterCounter -= 1;
         if (this.letterCounter === 0)
            this.letter = "";
         return nextLetter
      } else if (this.index == this.text.length) {
         return " "
      } else {
         return this._getNextLetter()
      }
   };

   /**
    * @param {}
    * @return {boolean}
    */
   hasNext() {
      return this.letterCounter || this.index < this.text.length
   };
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
