/**
 * Time complexity: O(1)
 * Auxiliary space complexity: O(1)
 * Tags: iterator
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
      if (this.letterCounter) {
         this.letterCounter--;
         return this.letter
      }
      this.letter = this.text[this.index];
      this.index++;

      while (
         this.index < this.text.length &&
         this.text[this.index].match(/\d/)
      ) {
         this.letterCounter = 10 * this.letterCounter + this.text[this.index];
         this.index++;
      }
      if (this.letterCounter) {
         this.letterCounter--;
         return this.letter
      }
   };

   /**
    * @param {}
    * @return {string}
    */
   next() {
      return this.hasNext() ? this._getNextLetter() : ' '
   };

   /**
    * @param {}
    * @return {boolean}
    */
   hasNext() {
      return this.letterCounter || this.index < this.text.length
   };
}


/**
 * O(1), O(1)
 * Design, Array, String, Iterator
 * generator
 */
class StringIterator {
   constructor(compressedString) {
      this.generator = this.generate(compressedString);
      this.letter = this._getNextLetter();
   }

   *generate(compressedString) {
      let index = 0;

      while (index < compressedString.length) {
         let letter = compressedString[index];
         index++;
         let frequency = 0;

         while (
            index < compressedString.length &&
            /\d/.test(compressedString[index])
         ) {
            frequency = 10 * frequency + Number(compressedString[index]);
            index++;
         }

         for (let f = 0; f < frequency; f++) {
            yield letter;
         }
      }
   }

   _getNextLetter() {
      const { value, done } = this.generator.next();
      return done ? ' ' : value;
   }

   next() {
      const currentLetter = this.letter;
      this.letter = this._getNextLetter();
      return currentLetter;
   }

   hasNext() {
      return this.letter !== ' ';
   }
}


const iterator = new StringIterator('L1e2t1C1o1d1e1')
console.log(iterator.next())  // return 'L'
console.log(iterator.next())  // return 'e'
console.log(iterator.next())  // return 'e'
console.log(iterator.next())  // return 't'
console.log(iterator.next())  // return 'C'
console.log(iterator.next())  // return 'o'
console.log(iterator.next())  // return 'd'
console.log(iterator.hasNext())  // return True
console.log(iterator.next())  // return 'e'
console.log(iterator.hasNext())  // return False
console.log(iterator.next())  // return ' '